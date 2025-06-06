import tkinter as tk
from banco import Banco

class Relatorio:
    def __init__(self, master):
        self.master = master
        self.db = Banco()
        self.build()

    def build(self):
        tk.Label(self.master, text="Relatório de Serviços", fg="#00f5ff", bg="black", font=("Arial", 14)).pack(pady=10)
        self.lista = tk.Listbox(self.master)
        self.lista.pack(fill="both", expand=True)
        self.preencher_lista()

    def preencher_lista(self):
        self.lista.delete(0, tk.END)
        for serv in self.db.listar_servicos():
            linha = " | ".join(map(str, serv))
            self.lista.insert(tk.END, linha)
