# A partir da idade informada por uma pessoa, elabore um algoritmo que informe a sua classe eleitoral
# sabendo que menores de 16 não votam, que o voto é obrigatório entre 18 e 65 anos, e opcional para 
# eleitores entre 16 e 18, e acima de 65 anos.

idade = int(input("Qual é a sua idade? "))
print("você está no grupo de ...")

if idade < 16:
  print("não votante.")
elif (idade >= 16 and idade < 18) or idade > 65:
  print("voto facultativo.")
else:
  print("voto obrigatório.")
