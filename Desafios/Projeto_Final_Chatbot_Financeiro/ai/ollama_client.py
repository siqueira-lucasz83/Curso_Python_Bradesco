import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"

def perguntar_ao_modelo(mensagens):
    payload = {
        "model": MODEL,
        "messages": mensagens,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]
