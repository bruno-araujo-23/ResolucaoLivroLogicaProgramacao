# Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano
# P(x1, y1) e Q(x2, y2), imprima a distância entre eles.

# determinando os pontos
x1 = float(input("Digite o ponto P 1: "))
y1 = float(input("Digite o ponto P 2: "))
x2 = float(input("Digite o ponto Q 1: "))
y2 = float(input("Digite o ponto Q 2: "))

# calculando a distância entre eles

d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(d)
