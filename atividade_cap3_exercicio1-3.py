# Faça um algoritmo para calcular o volume de uma esfera de raio R, em que R
# é um dado fornecido pelo usuário. 

# Determine o raio da esfera
raio = float(input("Qual é o raio da esfera? "))
# Calculo do volume
pi = 3.14159
volume = (4/3)*pi*raio**3
print(round(volume,3))