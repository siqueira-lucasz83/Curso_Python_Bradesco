# celso_furtado_notebooklm.py

import webbrowser

NOTEBOOK_LM_LINK = "https://notebooklm.google.com/notebook/05b47aa7-dca9-4a58-bf1f-0353d2863f9b"

def abrir():
    webbrowser.open(NOTEBOOK_LM_LINK)

def info():
    return "NotebookLM sobre Celso Furtado (posicionamento político e econômico)"

if __name__ == "__main__":
    print(info())

