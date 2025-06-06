import tkinter as tk
from tkinter import messagebox
from banco import Banco 

class Cadastro:
    def __init__(self, master):
        self.db = Banco()
        self.master = master
        self.build_form()
        self.listar()

    def build_form(self):
        campos = ["Cliente", "Problema", "Valor", "Data", "Status do Carro"]
        self.entries = {}
        for campo in campos:
            label = tk.Label(self.master, text=campo, fg="#00f5ff", bg="black")
            label.pack()
            entry = tk.Entry(self.master)
            entry.pack()
            self.entries[campo] = entry

        self.btn_salvar = tk.Button(self.master, text="Salvar", command=self.salvar, bg="#00f5ff")
        self.btn_salvar.pack(pady=5)

        self.btn_excluir = tk.Button(self.master, text="Excluir", command=self.excluir, bg="#00f5ff")
        self.btn_excluir.pack(pady=5)

        self.lista = tk.Listbox(self.master)
        self.lista.pack(fill="both", expand=True)
        self.lista.bind('<<ListboxSelect>>', self.selecionar)

    def salvar(self):
        dados = [self.entries[c].get() for c in self.entries]
        if all(dados):
            if hasattr(self, 'id_atual'):
                self.db.atualizar_servico(self.id_atual, *dados)
                del self.id_atual
            else:
                self.db.inserir_servico(*dados)
            self.limpar_campos()
            self.listar()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")

    def excluir(self):
        if hasattr(self, 'id_atual'):
            self.db.remover_servico(self.id_atual)
            del self.id_atual
            self.limpar_campos()
            self.listar()
        else:
            messagebox.showinfo("Info", "Selecione um item para excluir.")

    def selecionar(self, event):
        index = self.lista.curselection()
        if index:
            dados = self.lista.get(index)
            valores = dados.split(" | ")
            self.id_atual = int(valores[0])
            for i, campo in enumerate(self.entries):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, valores[i + 1])

    def listar(self):
        self.lista.delete(0, tk.END)
        for serv in self.db.listar_servicos():
            linha = " | ".join(map(str, serv))
            self.lista.insert(tk.END, linha)

    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
