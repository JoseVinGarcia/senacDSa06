import os

os.system("cls")

# EXEMPLO 1
mlista = []
mlista2 = [5, 3, 9, 4, 11]

print(f"Lista 2: {mlista2}")

# Acrescentar elemento no final e no começo
mlista.append(2) # adiciona no final o numero 2

mlista.insert(0, 5) # adiciona na posicao 0 o numero 5

print(f"Lista 1: {mlista}")

# INDEX: Encontra posição específica do numero escolhido

i = mlista2.index(11) # retorna a posicao do elemento

print(f"Posição 11 do i na lista 2: {i}")

# POSIÇÕES NA LISTA

print(f"\nPenúltimo elemento da lista 2: {mlista2[-2]}")
print(f"Último elemento da lista 2: {mlista2[-1]}")
print(f"Tamanho da lista 2: {len(mlista2)}")
print(f"Intervalo da lista 2: {mlista2[1:2]}") # Do índice 1 até ANTES do 2
print(f"Resto da lista 2 a partir de índice: {mlista2[1:]}") # Do índice 1 até todo o resto
print(f"Início da lista 2 até índice: {mlista2[:2]}") # Do início até o índice 2

# REMOVER ELEMENTO DA LISTA (Primeira ocorrencia - Primeiro valor em caso de repetido)

mlista2.remove(4) # remove o elemento

p = mlista2.pop(3) # remove 3 indice e mostra o elemento que foi removido

print(f"\nPop lista 2: {p}")
print(f"Lista 2 após remove e Pop: {mlista2}")

mlista.clear()
print(f"Lista após clear: {mlista}")

# LISTA DE TEXTO

mlista3 = "SENAC"

print(f"\nTexto: {mlista3}")
print(f"Tamanho do texto: {len(mlista3)}")
print(f"Indice do texto: {mlista3[1]}")

# ORGANIZACAO E TROCA DE POSIÇÃO EM LISTAS

mlista4 = ["c","a","b"]

print(f"\nLista 4: {mlista4}")

mlista4.reverse()

print(f"Lista revertida: {mlista4}")

mlista4.sort()

print(f"Lista ordenada: {mlista4}")
