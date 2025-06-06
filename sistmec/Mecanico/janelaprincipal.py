import tkinter as tk
from cadastro import Cadastro
from relatorio import Relatorio

class JPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Mecânico")
        self.root.geometry("800x500")
        self.root.configure(bg="black")

        self.frame_menu = tk.Frame(root, bg="#1e1e1e", width=200)
        self.frame_menu.pack(side="left", fill="y")

        self.frame_conteudo = tk.Frame(root, bg="black")
        self.frame_conteudo.pack(side="right", fill="both", expand=True)

        btn_cadastro = tk.Button(self.frame_menu, text="Cadastro", fg="#00f5ff", bg="#1e1e1e", command=self.abrircadastro)
        btn_cadastro.pack(fill="x", pady=10)

        btn_relatorio = tk.Button(self.frame_menu, text="Relatório", fg="#00f5ff", bg="#1e1e1e", command=self.abrirrelatorios)
        btn_relatorio.pack(fill="x", pady=10)

        self.abrircadastro()

    def abrircadastro(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()
        Cadastro(self.frame_conteudo)

    def abrirrelatorios(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()
        Relatorio(self.frame_conteudo)