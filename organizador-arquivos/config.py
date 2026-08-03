from pathlib import Path

PASTA_PADRAO = Path.home() / "Downloads"

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executáveis": [".exe", ".msi"],
    "Código": [".java", ".py", ".html", ".css", ".js", ".sql"]
}