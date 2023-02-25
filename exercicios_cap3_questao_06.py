# Um dado comerciante maluco cobra 10% de acréscimo para cada prestação em atraso e depois
# dá um desconto de 10% sobre essa valor. Faça um algoritmo que solicite o valor da prestação em atraso
# e apresente o valor final a pagar, assim como o prejuízo do comerciante.

valor_prestacao = float(input("Qual é o valor da prestação em atraso? "))
valor_final = valor_prestacao*1.1*0.9
prejuizo = valor_prestacao - valor_final

print(f"O valor final é {valor_final:.2f} reais. O prejuízo é {prejuizo:.2f} reais.")
