# Construa um algoritmo para calcular as raizes de uma equação do 2o grau
# (Ax² + Bx + C), sendo que os valores A, B e C são fornecidos pelo usuário

# parte 1 - determinar os valores de A, B e C

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# parte 2 - calcular delta

delta = B**2 - 4*A*C

if delta < 0:
    print("Não há raíz real!")

else:
    x1 = (-B + delta**(1/2))/2*A
    x2 = (-B - delta**(1/2))/2*A

    print("As raízes reais são:")
    print(x1)
    print(x2) 