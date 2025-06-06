import tkinter as tk
from tkinter import messagebox
from janelaprincipal import JPrincipal 

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x400")
        self.root.configure(bg='black')

        self.label = tk.Label(root, text="Usuário:", fg="#00f5ff", bg="black")
        self.label.pack(pady=10)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        self.button = tk.Button(root, text="Entrar", command=self.conferirlogin, bg="#00f5ff")
        self.button.pack(pady=20)

    def conferirlogin(self):
        usuario = self.entry.get()
        if usuario.strip():
            self.root.destroy()
            main_root = tk.Tk()
            JPrincipal(main_root)
            main_root.mainloop()
        else:
            messagebox.showerror("Erro", "Informe o nome do usuário.")
