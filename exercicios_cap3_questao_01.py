# Construa um algoritmo que calcule a média ponderada entre cinco números quaisquer,
# sendo que os pesos a serem aplicados são 1, 2, 3, 4 e 5 respectivamente.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
d = float(input("Digite o quarto número: "))
e = float(input("Digite o quinto número: "))

media_ponderada = ((a*1) + (b*2) + (c*3) + (d*4) + (e*5)) / 15

print(media_ponderada)
