import os

os.system("cls")

# EXEMPLO 1
senha = "54321"
leitura = ""

while leitura != senha:
    leitura = input("Digite a senha: ")
    if leitura == senha:
        print("Acesso liberado!")
    else:
        print("Senha Incorreta!")

# EXEMPLO 2 - LAÇO INFINITO

# i = 0
# while True:
#     print(i)
#     i +=1
# PARA QUEBRAR ESSE LOOP INFINITO CLIQUE NO TERMINAL DO VSCODE E DE CTRL + C

# EXEMPLO CONTAGEM REGRESSIVA

contador = 10
while contador != 0:
    print(contador)
    contador -= 1

# EXEMPLO CONTADOR
s = 0
c = 1

while c < 4:
    n = int(input("Informe um numero: "))
    s += n
    c += 1
print("O total é ", s)

# EXEMPLO TEXTO
n = ""
resposta = "S"

while resposta != "N":
    n = input("informe um texto: ")
    resposta = input("QUER CONTINUAR? S/N: ").upper()
print(n)

# EXEMPLO FINAL
n = s = 0 # PASSANDO O 0 PARA DUAS VARIAVEIS
while True:
    n = int(input("Numero: "))
    if n == 999:
        break
    s = s + n
print(s)
