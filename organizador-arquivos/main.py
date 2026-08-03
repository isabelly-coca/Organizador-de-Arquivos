from pathlib import Path
import shutil

# Caminho da pasta Downloads
downloads = Path.home() / "Downloads"

# Dicionário com as extensões e suas respectivas pastas
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"]
}

# Cria as pastas, caso não existam
for pasta in categorias.keys():
    (downloads / pasta).mkdir(exist_ok=True)

# Percorre todos os arquivos da pasta Downloads
for arquivo in downloads.iterdir():

    # Ignora as pastas
    if arquivo.is_dir():
        continue

    # Obtém a extensão do arquivo
    extensao = arquivo.suffix.lower()

    # Procura em qual categoria a extensão pertence
    for pasta, extensoes in categorias.items():

        if extensao in extensoes:
            destino = downloads / pasta / arquivo.name

            shutil.move(str(arquivo), str(destino))

            print(f"{arquivo.name} → {pasta}")

            break

print("\nOrganização concluída!")