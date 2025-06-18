distancia = int
combustivel = float
consumo = float

distancia = int(input("Distancia percorrida:"))
combustivel_str = input("Combustivel gasto:")
combustivel = float(combustivel_str.replace(',', '.'))
consumo = 0

consumo = (distancia / combustivel)
print(f"Consumo médio: {consumo:.3f}")
