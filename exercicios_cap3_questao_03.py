# Prepare um algoritmo capaz de inverter um número de três dígitos fornecidos, ou seja,
# apresentar primeiro a unidade, depois a dezena e a centena.

numero = str(input("Digite um número com 3 dígitos: "))
num = []

if len(numero)==3:
  for i in range(2, -1, -1):
    num.append(numero[i])
  novo_num = ''.join(num)
  print(int(novo_num))
else:
  print("Você não digitou um número com 3 dígitos...")
