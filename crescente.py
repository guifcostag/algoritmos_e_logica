x = int
y = int

x = int(input("Digite dois números: "))
y = int(input(""))

while x != y:
  if x < y:
    print("Crescente")
  else:
    print("Decrescente")

  x = int(input("Digite dois números: "))
  y = int(input(""))
