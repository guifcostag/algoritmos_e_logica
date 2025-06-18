import math

m: int
n: int
somapositivos: int
linha: int
coluna: int

n = int(input("Qual a ordem da matriz?"))
m = n

matriz: [[float]] = [[0 for x in range (n)] for x in range (n)]

for i in range (m):
  for j in range (n):
    matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

somapositivos = 0;
for i in range (m):
    for j in range (n):
        if matriz[i][j] > 0:
            somapositivos += matriz[i][j]

print(f"\nSoma dos positivos = {somapositivos};\n")

linha = int(input("Escolha uma linha: "))

print("Linha escolhida:", end="");

for i in range (m):
  print(f"{matriz[linha][i]},  ", end="")

print("", end="")
coluna = int(input("\nEscolha uma coluna: "))

print("Coluna escolhida: ", end="");

for i in range (n):
  print(f"{matriz[i][coluna]},  ", end="")

print("", end="")
print("\nDiagonal principal: ", end="")
for i in range (m):
    for j in range (n):
        if i == j:
            print(f"{matriz[i][j]}, ")

for i in range (m):
  for j in range (n):
    if matriz[i][j] < 0:
      matriz[i][j] =  matriz[i][j] * matriz[i][j]

print("\nMatriz modificada: \n")
for i in range (m):
  for j in range (n):
    print(f"{matriz[i][j]},  ", end="")
  print()
