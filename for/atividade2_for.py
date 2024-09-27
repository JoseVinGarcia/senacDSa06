import os

os.system("cls")

# EXEMPLO

previsoes = ["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]

PREVISAO_BOA = "Ensolarado"

for e in previsoes:
    if e == PREVISAO_BOA:
        print(f"{e}: Aproveite e passeie!")
    else:
        print(f"{e}: Prepare o guarda-chuva!")
