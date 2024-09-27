import os

os.system("cls")

# ATIVIDADE 1
print("_"*30)
print("Olá, tudo bem? Vamos criar uma lista de compras.")

mlista = []

i1 = input("Insira sua primeira compra: ")
i2 = input("Insira sua segunda compra: ")
i3 = input("Insira sua terceira compra: ")

# gambiarra
mlista.append(i1)
mlista.append(i2)
mlista.append(i3)

print(f"Essa é sua lista: {mlista}")

print("\nO que deseja fazer agora?\n[0] Comprar água\n[1] Remover Objeto\n[2] Organizar Carrinho")
numero=int(input("Digite sua opção: "))

match numero:
    case 0:
        mlista.append("Água")
    case 1:
        mlista.remove(mlista[-1])
    case 2:
        mlista.sort()
    case _:
        print("Operação inválida")

print(f"No final, essa ficou sua lista: {mlista}")