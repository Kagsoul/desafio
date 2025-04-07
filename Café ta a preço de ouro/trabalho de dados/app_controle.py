import tkinter as S
from tkinter import messagebox as MB
import datetime as horas
from tkinter import ttk as Tk
from salario import controle

class controle:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salário")
        self.root.geometry("500x680")
        self.root.config(bg="#f0f0f0")

        self.historico = []

        frame = S.Frame(root, bg="#f0f0f0")
        frame.pack(padx=20, pady=20)

        self.nome_label = S.Label(frame, text="Digite seu nome:", bg="#f0f0f0", font=("Arial", 12))
        self.nome_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.nome_entry = S.Entry(frame, font=("Arial", 12))
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.valor_hora_label = S.Label(frame, text="Pagamento por hora (R$):", bg="#f0f0f0", font=("Arial", 12))
        self.valor_hora_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.valor_hora_entry = S.Entry(frame, font=("Arial", 12))
        self.valor_hora_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.horas_extras_label = S.Label(frame, text="Horas extras trabalhadas:", bg="#f0f0f0", font=("Arial", 12))
        self.horas_extras_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.horas_extras_entry = S.Entry(frame, font=("Arial", 12))
        self.horas_extras_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.valor_hora_extra_label = S.Label(frame, text="Salário hora extra (R$):", bg="#f0f0f0", font=("Arial", 12))
        self.valor_hora_extra_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        self.valor_hora_extra_entry = S.Entry(frame, font=("Arial", 12))
        self.valor_hora_extra_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.dias_trabalho_label = S.Label(frame, text="Número de dias trabalhados no mês:", bg="#f0f0f0", font=("Arial", 12))
        self.dias_trabalho_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.dias_trabalho_entry = S.Entry(frame, font=("Arial", 12))
        self.dias_trabalho_entry.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.sindicato_label = S.Label(frame, text="Pagamento para o Sindicato (R$):", bg="#f0f0f0", font=("Arial", 12))
        self.sindicato_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)

        self.sindicato_entry = S.Entry(frame, font=("Arial", 12))
        self.sindicato_entry.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.vale_transporte_label = S.Label(frame, text="Pagar transporte (R$):", bg="#f0f0f0", font=("Arial", 12))
        self.vale_transporte_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)

        self.vale_transporte_entry = S.Entry(frame, font=("Arial", 12))
        self.vale_transporte_entry.grid(row=6, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.vale_refeicao_label = S.Label(frame, text="Gasto de Vale/Refeição (R$):", bg="#f0f0f0", font=("Arial", 12))
        self.vale_refeicao_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)

        self.vale_refeicao_entry = S.Entry(frame, font=("Arial", 12))
        self.vale_refeicao_entry.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.calcular_button = S.Button(frame, text="Calcular Salário", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.calcular_salario)
        self.calcular_button.grid(row=8, columnspan=2, pady=10)

        self.resultado_label = S.Label(root, text="", justify="left", font=("Arial", 12), bg="#f0f0f0", width=60, height=10, relief="solid", anchor="w", padx=10, pady=10)
        self.resultado_label.pack(padx=20, pady=20)

    def validar_entrada(self, valor):
        try:
            return float(valor)
        except ValueError:
            return -1

    def calcular_salario(self):
        nome = self.nome_entry.get()
        valor_por_hora = self.validar_entrada(self.valor_hora_entry.get())
        horas_extras = self.validar_entrada(self.horas_extras_entry.get())
        valor_hora_extra = self.validar_entrada(self.valor_hora_extra_entry.get())
        dias_trabalho = self.validar_entrada(self.dias_trabalho_entry.get())
        sindicato = self.validar_entrada(self.sindicato_entry.get())
        vale_transporte = self.validar_entrada(self.vale_transporte_entry.get())
        vale_refeicao = self.validar_entrada(self.vale_refeicao_entry.get())

        if valor_por_hora < 0 or horas_extras < 0 or valor_hora_extra < 0 or dias_trabalho < 1 or dias_trabalho > 31:
            MB.showerror("Erro", "Por favor, insira valores válidos!")
            return

        horas_por_dia = 8
        salario_bruto = valor_por_hora * horas_por_dia * dias_trabalho
        salario_bruto += valor_hora_extra * horas_extras

        irrf = 8 / 100
        inss = 5 / 100
        valor_irrf = salario_bruto * irrf
        valor_inss = salario_bruto * inss

        salario_liquido = salario_bruto - (valor_irrf + valor_inss + sindicato + vale_transporte + vale_refeicao)

        resultado = f"""
        Nome: {nome}
        Salário Bruto: R${salario_bruto:.2f}
        IRRF (8%): R${valor_irrf:.2f}
        INSS (5%): R${valor_inss:.2f}
        Sindicato: R${sindicato:.2f}
        Vale Transporte: R${vale_transporte:.2f}
        Vale Refeição: R${vale_refeicao:.2f}
        Salário Líquido: R${salario_liquido:.2f}
        Horas Extras: {horas_extras} horas
        Valor Hora Extra: R${valor_hora_extra:.2f}
        """
        
        self.resultado_label.config(text=resultado)

        self.historico.append({
            'Nome': nome,
            'Salário Bruto': salario_bruto,
            'IRRF': valor_irrf,
            'INSS': valor_inss,
            'Sindicato': sindicato,
            'Vale Transporte': vale_transporte,
            'Vale Refeição': vale_refeicao,
            'Salário Líquido': salario_liquido,
            'Horas Extras': horas_extras,
            'Valor Hora Extra': valor_hora_extra,
            'Data de Cálculo': horas.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })


root = S.Tk()
app = controle(root)
root.mainloop()
