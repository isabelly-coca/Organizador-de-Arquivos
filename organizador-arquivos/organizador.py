import shutil

from config import CATEGORIAS
from logger import registrar


def organizar(downloads):

    mensagens = []

    for pasta in CATEGORIAS.keys():
        (downloads / pasta).mkdir(exist_ok=True)

    (downloads / "Outros").mkdir(exist_ok=True)

    for arquivo in downloads.iterdir():

        if arquivo.is_dir():
            continue

        extensao = arquivo.suffix.lower()

        encontrado = False

        for pasta, extensoes in CATEGORIAS.items():

            if extensao in extensoes:

                destino = downloads / pasta / arquivo.name

                shutil.move(str(arquivo), str(destino))

                mensagem = f"✔ {arquivo.name} → {pasta}"

                mensagens.append(mensagem)

                registrar(mensagem)

                encontrado = True

                break

        if not encontrado:

            destino = downloads / "Outros" / arquivo.name

            shutil.move(str(arquivo), str(destino))

            mensagem = f"✔ {arquivo.name} → Outros"

            mensagens.append(mensagem)

            registrar(mensagem)

    return mensagens