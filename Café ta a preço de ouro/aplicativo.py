import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def abrir_app_dados():
    try:
        subprocess.run(['python', os.path.join('trabalho de dados', 'app_dados.py')], check=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao abrir o App Dados: {e}")

def abrir_app_salario():
    try:
        subprocess.run(['python', os.path.join('trabalho de dados', 'salario', 'arquivo', 'app.py')], check=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao abrir o App Salário: {e}")

def abrir_app_controle_opcao1():
    try:
        caminho_app_controle = os.path.join('trabalho de dados', 'app_controle.py')
        if not os.path.exists(caminho_app_controle):
            raise FileNotFoundError(f"O arquivo {caminho_app_controle} não foi encontrado.")
        subprocess.run(['python', caminho_app_controle, '--opcao', '1'], check=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao abrir o App Controle : {e}")

def abrir_app_controle_opcao2():
    try:
        caminho_app_controle = os.path.join('trabalho de dados', 'app_controle.py')
        if not os.path.exists(caminho_app_controle):
            raise FileNotFoundError(f"O arquivo {caminho_app_controle} não foi encontrado.")
        subprocess.run(['python', caminho_app_controle, '--opcao', '2'], check=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao abrir o App Controle : {e}")

def criar_interface():
    raiz = tk.Tk()
    raiz.title("Launcher de Aplicativos")
    raiz.geometry("600x550")
    raiz.configure(bg="#2c3e50")

    frame_cabecalho = tk.Frame(raiz, bg="#34495e", height=100)
    frame_cabecalho.pack(fill=tk.X)
    label_cabecalho = tk.Label(
        frame_cabecalho,
        text="dados e Controle de salario",
        font=("Helvetica", 24, "bold"),
        fg="white",
        bg="#34495e",
        pady=20
    )
    label_cabecalho.pack()

    frame_conteudo = tk.Frame(raiz, bg="#2c3e50")
    frame_conteudo.pack(expand=True, padx=20, pady=20)

    label_instrucoes = tk.Label(
        frame_conteudo,
        text="Selecione o aplicativo que deseja abrir:",
        font=("Helvetica", 16),
        fg="white",
        bg="#2c3e50",
        pady=10
    )
    label_instrucoes.pack()

    botao_dados = tk.Button(
        frame_conteudo,
        text="Abrir: Cadastro de Dados",
        command=abrir_app_dados,
        font=("Helvetica", 14),
        bg="#3498db",
        fg="white",
        width=30,
        height=2,
        relief="groove",
        bd=4
    )
    botao_dados.pack(pady=15)


    botao_controle_opcao1 = tk.Button(
        frame_conteudo,
        text="Abrir: Controle de salario",
        command=abrir_app_controle_opcao1,
        font=("Helvetica", 14),
        bg="#1abc9c",
        fg="white",
        width=30,
        height=2,
        relief="groove",
        bd=4
    )
    botao_controle_opcao1.pack(pady=15)

    botao_sair = tk.Button(
        frame_conteudo,
        text="Sair do Launcher",
        command=raiz.quit,
        font=("Helvetica", 12, "bold"),
        bg="#e74c3c",
        fg="white",
        width=20,
        height=2,
        relief="groove",
        bd=4
    )
    botao_sair.pack(pady=30)

    frame_rodape = tk.Frame(raiz, bg="#34495e", height=50)
    frame_rodape.pack(fill=tk.X, side=tk.BOTTOM)
    label_rodape = tk.Label(
        frame_rodape,
        text="Criado com carinho por Kagsoul, Empresa: Brasil Gamezil",
        font=("Helvetica", 10),
        fg="white",
        bg="#34495e"
    )
    label_rodape.pack(pady=10)

    raiz.mainloop()

if __name__ == "__main__":
    criar_interface()