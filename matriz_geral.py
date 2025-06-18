import math

# Declarando variáveis
m: int
n: int
somapositivos: int
linha: int
coluna: int

# Pergunta inicial e criação da matriz
n = int(input("Qual a ordem da matriz?"))
m = n

matriz: [[float]] = [[0 for x in range (n)] for x in range (n)]

# Preenchendo a matriz
for i in range (m):
  for j in range (n):
    matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

# Calculando a soma dos positivos
somapositivos = 0;
for i in range (m):
    for j in range (n):
        if matriz[i][j] > 0:
            somapositivos += matriz[i][j]

print(f"\nSoma dos positivos = {somapositivos};\n")

# Imprimindo elementos de uma linha
linha = int(input("Escolha uma linha: "))

print("Linha escolhida:", end="");

for i in range (m):
  print(f"{matriz[linha][i]},  ", end="")

print("", end="")

# Imprimindo elementos de uma coluna
coluna = int(input("\nEscolha uma coluna: "))

print("Coluna escolhida: ", end="");

for i in range (n):
  print(f"{matriz[i][coluna]},  ", end="")

print("", end="")

# Diagonal principal
print("\nDiagonal principal: ", end="")
for i in range (m):
    for j in range (n):
        if i == j:
            print(f"{matriz[i][j]}, ")

for i in range (m):
  for j in range (n):
    if matriz[i][j] < 0:
      matriz[i][j] =  matriz[i][j] * matriz[i][j]

# Alterando valores negativos
print("\nMatriz modificada: \n")
for i in range (m):
  for j in range (n):
    print(f"{matriz[i][j]},  ", end="")
  print()
