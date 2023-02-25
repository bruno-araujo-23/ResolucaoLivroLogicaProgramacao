# Dada uma data de aniversário (dia, mês e ano), elabore um algoritmo que solicite a data atual
# e calcule a idade em anos, meses e dias.

dia_nasc = int(input("Qual é o dia do seu nascimento? "))
mes_nasc = int(input("Qual é o mes do seu nascimento? "))
ano_nasc = int(input("Qual é o ano do seu nascimento? "))
dia_hoje = int(input("Que dia é hoje? "))
mes_hoje = int(input("Que mes estamos? "))
ano_hoje = int(input("Que ano estamos? "))

# Calculando o ano
ano = ano_hoje - ano_nasc

# Calculando o mês
if mes_nasc < mes_hoje:
  mes = mes_hoje - mes_nasc
elif mes_nasc > mes_hoje:
  ano -= 1
  mes = 12 - (mes_nasc - mes_hoje)
else:
  mes = 0

# Calculando o dia2
if dia_nasc < dia_hoje:
  dia = dia_hoje - dia_nasc
elif dia_nasc > dia_hoje:
    mes = 11
    if mes_hoje == 1 or mes_hoje == 3 or mes_hoje == 5 or mes_hoje == 7 or mes_hoje == 8 or mes_hoje == 10 or mes_hoje == 12:
      dia = 31 - (dia_nasc - dia_hoje)
    elif mes_hoje == 4 or mes_hoje == 6 or mes_hoje == 9 or mes_hoje == 11:
      dia = 30 - (dia_nasc - dia_hoje)
    else:
      if ano % 4 == 0:
        dia = 29 - (dia_nasc - dia_hoje)
      else:
        dia = 28 - (dia_nasc - dia_hoje)
else:
  dia = 0

print("A idade da pessoa é...")
print(f"{ano} anos, {mes} meses e {dia} dias.")
