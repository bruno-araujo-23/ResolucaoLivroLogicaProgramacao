# Elabore um algoritmo que, a partir de uma data, verifique sua validade.
# Considere os dias com 30 e 31 dias e os anos bissextos.

dia = int(input("digite um dia: "))
mes = int(input("digite um mes: "))
ano = int(input("digite um ano: "))

if dia > 31 or mes > 13:
  print("data inválida")
elif dia == 0 or mes == 0 or ano == 0:
  print("data inválida")
elif ano % 4 == 0:
  if dia > 29 and mes == 2:
    print("data inválida")
  else:
    print("data válida")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  if dia>30:
    print("data inválida")
  else:
    print('data válida')
elif mes == 2:
  if dia>28:
    print('data inválida')
  else:
    print("data válida")
