import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

from organizador import organizar

# Configuração da aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()
app.title("Organizador Inteligente de Arquivos")
app.geometry("700x600")
app.resizable(False, False)

pasta = None


def selecionar_pasta():
    global pasta

    pasta = filedialog.askdirectory()

    if pasta:
        label.configure(
            text=f"📂 Pasta selecionada:\n{pasta}"
        )


def iniciar():

    if not pasta:
        label.configure(text="⚠ Selecione uma pasta primeiro.")
        return

    resultado = organizar(Path(pasta))

    quantidade = len(resultado)

    label.configure(
        text=f"✅ Organização concluída!\n\n{quantidade} arquivo(s) organizado(s)."
    )

    texto.configure(state="normal")
    texto.delete("1.0", "end")

    if quantidade == 0:
        texto.insert(
            "end",
            "Nenhum arquivo encontrado para organizar."
        )
    else:
        for linha in resultado:
            texto.insert("end", linha + "\n")

    texto.configure(state="disabled")


# =======================
# Título
# =======================

titulo = ctk.CTkLabel(
    app,
    text="📂 Organizador Inteligente de Arquivos",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=(20, 10))

descricao = ctk.CTkLabel(
    app,
    text="Organize automaticamente seus arquivos por categoria.",
    font=("Arial", 14)
)

descricao.pack(pady=(0, 20))

# =======================
# Botões
# =======================

botao1 = ctk.CTkButton(
    app,
    text="📁 Selecionar Pasta",
    width=250,
    height=45,
    command=selecionar_pasta
)

botao1.pack(pady=10)

botao2 = ctk.CTkButton(
    app,
    text="🚀 Organizar Arquivos",
    width=250,
    height=45,
    command=iniciar
)

botao2.pack(pady=10)

# =======================
# Status
# =======================

label = ctk.CTkLabel(
    app,
    text="📂 Nenhuma pasta selecionada",
    font=("Arial", 13)
)

label.pack(pady=15)

# =======================
# Resultado
# =======================

resultado_label = ctk.CTkLabel(
    app,
    text="Arquivos organizados",
    font=("Arial", 16, "bold")
)

resultado_label.pack(pady=(20, 5))

texto = ctk.CTkTextbox(
    app,
    width=620,
    height=220,
    font=("Consolas", 14)
)

texto.pack(pady=10)

texto.configure(state="disabled")

# =======================

app.mainloop()