# Ao completar um tanque de combustível de um automóvel, faça um algoritmo que calcule 
# o consumo efetuado, assim como a autonomia que o carro ainda teria antes do abastecimento.
# Considere que o veículo sempre seja abastecido até completar o tanque e que sejam fornecidas 
# apenas a capacidade do tanque, a quantidade de litros abastecida e a quilometragem percorrida
# desde o último abastecimento.

volume_anterior = float(input("Qual o volume antes de abastecer? "))
capacidade_tanque = float(input("Qual é a capacidade do tanque? "))
volume_abastecido = capacidade_tanque - volume_anterior
quilometragem_percorrida = float(input("Qual foi a quilometragem percorrida desde o último abastecimento? "))
autonomia = quilometragem_percorrida / volume_abastecido

print(f"o consumo efetuado foi {volume_abastecido} litros, e a autonomia do carro é {autonomia:.2f} km/litro")
