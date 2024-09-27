import os

os.system("cls")

# ATIVIDADES

# Atividade 1
for b in range(10, -1, -1):
    print(b)

# Atividade 2

val = int(input("Digite seu valor: "))

for i in range(1, val+1):
    if val % i == 0:
        print(i)
