# Declarando variáveis
m: int
n: int

# Pergunta inicial com atribuição às variáveis
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

# Declarando a matriz
matriz: [[int]] = [[0 for x in range (n)] for x in range (m)]

# Preenchendo a matriz
for i in range (m):
    for j in range (n):
        matriz [i][j] = int(input(f"Elemento [{i},{j}]: "))

# Capturando os valores negativos da matriz
print("\nValores Negativos: ")
for i in range (m):
    for j in range (n):
        if matriz [i][j] < 0:
            print(matriz [i][j])
