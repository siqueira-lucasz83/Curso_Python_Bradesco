import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import soundfile as sf
from gtts import gTTS
from dotenv import load_dotenv
import openai
import tempfile

# Carregar variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SAMPLE_RATE = 44100
DURATION = 5  # segundos

def gravar_audio():
    print("🎤 Gravando... Fale agora!")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    print("✅ Gravação finalizada!")
    return audio

def salvar_audio(audio):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wavfile.write(temp_file.name, SAMPLE_RATE, audio)
    return temp_file.name

def transcrever_audio(caminho_audio):
    with open(caminho_audio, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def perguntar_chatgpt(texto):
    resposta = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": texto}
        ]
    )
    return resposta.choices[0].message.content

def falar_texto(texto):
    tts = gTTS(text=texto, lang='pt')
    temp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_mp3.name)

    # Converter MP3 para WAV e tocar
    data, samplerate = sf.read(temp_mp3.name)
    print("🔊 Reproduzindo resposta...")
    sd.play(data, samplerate)
    sd.wait()

def main():
    audio = gravar_audio()
    caminho_audio = salvar_audio(audio)
    texto_usuario = transcrever_audio(caminho_audio)

    print(f"📝 Você disse: {texto_usuario}")

    resposta = perguntar_chatgpt(texto_usuario)
    print(f"🤖 ChatGPT: {resposta}")

    falar_texto(resposta)

if __name__ == "__main__":
    main()
