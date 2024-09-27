import os

os.system("cls")

# EXEMPLO
# O Apelido no for sempre começa como 0

for a in range(5, 10): # Imprime do 5 até antes do 10
    print(a)

for b in range(0, 100, 5): # Imprime do 0 até o 100, pulando de 5
    print(b)

var = "PYTHON"
for c in var: # Imprime as letras
    print(c)

llista = ["Olá", 1, 2.0]
for d in llista: # Imprime a lista
    print(d)

# Caso mais complexo

i = int(input("Valor: "))
f = int(input("Fim: "))

for e in range(i,f+1): # F+1 para contar tambem o numero inserido
    print(e)

# Caso 2

s = 0

for n in range(5):
    i = int(input("Valor: "))
    s = s + i

print(f"A soma é {s}")
