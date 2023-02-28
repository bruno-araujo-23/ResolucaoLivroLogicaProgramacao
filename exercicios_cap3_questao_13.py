# Elabore um algoritmo que obtenha o mínimo múltiplo comum (MMC) entre dois números.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
fatora1 = []
fatora2 = []
mmc = 1

for numero in numeros_primos:
  while numero1 % numero == 0:
    numero1 /= numero
    fatora1.append(numero)
  while numero2 % numero == 0:
    numero2 /= numero
    fatora2.append(numero)

print(fatora1)
print(fatora2)

for numero in numeros_primos:
  if fatora1.count(numero) > 0 or fatora2.count(numero) > 0:
    if fatora1.count(numero) >= fatora2.count(numero):
      mmc = mmc*numero**fatora1.count(numero)
    elif fatora2.count(numero) > fatora1.count(numero):
      mmc = mmc*numero**fatora2.count(numero)

print(mmc)
