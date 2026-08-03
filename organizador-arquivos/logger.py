from pathlib import Path
from datetime import datetime

LOGS = Path("logs")
LOGS.mkdir(exist_ok=True)

ARQUIVO_LOG = LOGS / "organizacao.log"

def registrar(mensagem):
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"[{data}] {mensagem}\n")