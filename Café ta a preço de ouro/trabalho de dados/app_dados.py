import sys as Sistema
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class Habitante:
    def __init__(self, nome, sexo, cor_olhos, cor_cabelos, idade):
        self.nome = nome
        self.sexo = sexo
        self.cor_olhos = cor_olhos
        self.cor_cabelos = cor_cabelos
        self.idade = idade

class Sistema:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.habitantes = self.carregar_habitantes()

    def carregar_habitantes(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                return [Habitante(**habitante) for habitante in dados]
        return []

    def salvar_habitantes(self):
        dados = [habitante.__dict__ for habitante in self.habitantes]
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

    def adicionar_habitante(self, habitante):
        self.habitantes.append(habitante)
        self.salvar_habitantes()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de analise do Habitantes")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        
        self.sistema = Sistema("Pessoas_dados.json")

        self.font_label = ('Arial', 12, 'bold')
        self.font_entry = ('Arial', 12)
        self.font_button = ('Arial', 14, 'bold')

        self.header_label = tk.Label(self.root, text="Cadastro de dados dos Habitantes", font=('Arial', 18, 'bold'), fg="#005b96", bg="#f0f0f0")
        self.header_label.pack(pady=20)

        self.nome_label = tk.Label(self.root, text="Nome:", font=self.font_label, bg="#f0f0f0")
        self.nome_label.pack(pady=5)
        self.nome_entry = tk.Entry(self.root, font=self.font_entry, width=40, bd=2, relief="solid")
        self.nome_entry.pack(pady=5)

        self.sexo_label = tk.Label(self.root, text="Sexo (masculino ou feminino | F ou M):", font=self.font_label, bg="#f0f0f0")
        self.sexo_label.pack(pady=5)
        self.sexo_entry = tk.Entry(self.root, font=self.font_entry, width=40, bd=2, relief="solid")
        self.sexo_entry.pack(pady=5)

        self.idade_label = tk.Label(self.root, text="Idade (deve ser maior que 18):", font=self.font_label, bg="#f0f0f0")
        self.idade_label.pack(pady=5)
        self.idade_entry = tk.Entry(self.root, font=self.font_entry, width=40, bd=2, relief="solid")
        self.idade_entry.pack(pady=5)

        self.cor_cabelos_label = tk.Label(self.root, text="Cor dos cabelos:", font=self.font_label, bg="#f0f0f0")
        self.cor_cabelos_label.pack(pady=5)
        self.cor_cabelos_entry = tk.Entry(self.root, font=self.font_entry, width=40, bd=2, relief="solid")
        self.cor_cabelos_entry.pack(pady=5)

        self.cor_olhos_label = tk.Label(self.root, text="Cor dos olhos:", font=self.font_label, bg="#f0f0f0")
        self.cor_olhos_label.pack(pady=5)
        self.cor_olhos_entry = tk.Entry(self.root, font=self.font_entry, width=40, bd=2, relief="solid")
        self.cor_olhos_entry.pack(pady=5)

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar dados do habitante", font=self.font_button, fg="white", bg="#005b96", width=30, height=2, command=self.cadastrar_habitante)
        self.cadastrar_button.pack(pady=20)

        self.visualizar_button = tk.Button(self.root, text="Visualizar Dados", font=self.font_button, fg="white", bg="#005b96", width=30, height=2, command=self.visualizar_habitantes)
        self.visualizar_button.pack(pady=10)

    def cadastrar_habitante(self):
        nome = self.nome_entry.get()
        sexo = self.sexo_entry.get().strip().lower()
        idade = self.idade_entry.get()
        cor_cabelos = self.cor_cabelos_entry.get()
        cor_olhos = self.cor_olhos_entry.get()
        
        if not nome or not sexo or not idade or not cor_cabelos or not cor_olhos:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        if not idade.isdigit():
            messagebox.showerror("Erro", "Idade deve ser um número válido!")
            return
        idade = int(idade)
        if idade <= 17:
            messagebox.showerror("Erro", "Idade deve ser maior que 18 anos!")
            return

        if sexo not in ["masculino", "feminino", "m", "f"]:
            messagebox.showerror("Erro", "Sexo deve ser 'masculino', 'feminino', 'M' ou 'F'")
            return
        if sexo == "m" or sexo == "masculino":
         sexo = "MASCULINO"
        elif sexo == "f" or sexo == "feminino":
           sexo = "FEMININO"

        habitante = Habitante(nome, sexo, cor_olhos, cor_cabelos, idade)
        self.sistema.adicionar_habitante(habitante)
        messagebox.showinfo("Sucesso", f"Habitante {nome} registrado com sucesso!")

    def visualizar_habitantes(self):
        root_visualizar = tk.Toplevel(self.root)
        root_visualizar.title("Registrados de Dados| Mais informação ao abrir a janela")
        root_visualizar.geometry("200x400") 
        root_visualizar.configure(bg="#f0f0f0")

        pesquisa_label = tk.Label(root_visualizar, text="Mais informação ao abrir a janela:", bg="#f0f0f0")
        pesquisa_label.pack(pady=5)

        pesquisa_nome = tk.BooleanVar(value=True)
        pesquisa_sexo = tk.BooleanVar(value=True)
        pesquisa_idade = tk.BooleanVar(value=True)
        pesquisa_cor_cabelos = tk.BooleanVar(value=True)
        pesquisa_cor_olhos = tk.BooleanVar(value=True)

        tk.Checkbutton(root_visualizar, text="Nome", variable=pesquisa_nome, bg="#f0f0f0").pack(anchor=tk.W)
        tk.Checkbutton(root_visualizar, text="Sexo", variable=pesquisa_sexo, bg="#f0f0f0").pack(anchor=tk.W)
        tk.Checkbutton(root_visualizar, text="Idade", variable=pesquisa_idade, bg="#f0f0f0").pack(anchor=tk.W)
        tk.Checkbutton(root_visualizar, text="Cor dos Cabelos", variable=pesquisa_cor_cabelos, bg="#f0f0f0").pack(anchor=tk.W)
        tk.Checkbutton(root_visualizar, text="Cor dos Olhos", variable=pesquisa_cor_olhos, bg="#f0f0f0").pack(anchor=tk.W)

        pesquisa_entry = tk.Entry(root_visualizar)
        pesquisa_entry.pack(pady=10)

        def filtrar_habitantes():
            termo_pesquisa = pesquisa_entry.get().lower()

            for item in tree.get_children():
                tree.delete(item)

            for habitante in self.sistema.habitantes:
                nome = habitante.nome if hasattr(habitante, 'nome') else "Desconhecido"
                sexo = habitante.sexo if hasattr(habitante, 'sexo') else "Desconhecido"
                idade = habitante.idade if hasattr(habitante, 'idade') else "Desconhecido"
                cor_cabelos = habitante.cor_cabelos if hasattr(habitante, 'cor_cabelos') else "Desconhecida"
                cor_olhos = habitante.cor_olhos if hasattr(habitante, 'cor_olhos') else "Desconhecida"
                
                if ((pesquisa_nome.get() and termo_pesquisa in nome.lower()) or
                    (pesquisa_sexo.get() and termo_pesquisa in sexo.lower()) or
                    (pesquisa_idade.get() and termo_pesquisa in str(idade).lower()) or
                    (pesquisa_cor_cabelos.get() and termo_pesquisa in cor_cabelos.lower()) or
                    (pesquisa_cor_olhos.get() and termo_pesquisa in cor_olhos.lower())):
                    tree.insert("", "end", values=(nome, sexo, idade, cor_cabelos, cor_olhos))

        pesquisa_button = tk.Button(root_visualizar, text="Pesquisar", command=filtrar_habitantes)
        pesquisa_button.pack(pady=2)

        tree = ttk.Treeview(root_visualizar, columns=("Nome", "Sexo", "Idade", "Cor dos Cabelos", "Cor dos Olhos"), show="headings")
        
        tree.heading("Nome", text="Nome")
        tree.heading("Sexo", text="Sexo")
        tree.heading("Idade", text="Idade")
        tree.heading("Cor dos Cabelos", text="Cor dos Cabelos")
        tree.heading("Cor dos Olhos", text="Cor dos Olhos")

        tree.column("Nome", width=200)
        tree.column("Sexo", width=50)
        tree.column("Idade", width=50)
        tree.column("Cor dos Cabelos", width=150)
        tree.column("Cor dos Olhos", width=150)

        frame = tk.Frame(root_visualizar)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)

        filtrar_habitantes()


root = tk.Tk()
app = App(root)
root.mainloop()
