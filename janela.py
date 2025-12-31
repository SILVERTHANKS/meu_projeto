import tkinter as tk

# Criar janela principal
janela = tk.Tk()
janela.title('Olá, seja bem-vindo')
janela.geometry('400x300')

# Label inicial
label = tk.Label(janela, text="Digite seu nome:")
label.pack(pady=10)

# Caixa de entrada de texto
entrada_texto = tk.Entry(janela)
entrada_texto.pack(pady=5)

# Função chamada ao clicar no botão
def resposta():
    nome = entrada_texto.get()
    label.config(text=f"Seja bem-vindo, {nome}!")

# Botão que chama a função resposta
botao = tk.Button(janela, text="Clique aqui", command=resposta)
botao.pack(pady=10)

# Iniciar loop da janela
janela.mainloop()
   