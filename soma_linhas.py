m: int
n: int

m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

matriz: [[float]] = [[0 for x in range (n)] for x in range (m)]
vet: [float] = [0 for x in range (m)]

for i in range (m):
    for j in range (n):
        matriz[i][j] = float(input(f"Digite o valor da posição [{i},{j}]: ")) 

for i in range (m):
    soma = 0
    for j in range (n):
        soma += matriz[i][j]
    vet[i] = soma

print("\nVETOR GERADO:")
print(f"{vet}")
