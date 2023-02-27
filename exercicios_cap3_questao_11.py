# Construa um algoritmo capaz de dar a classificação olímpica de três países informados.
# Para cada país é informado o nome e a quantidade de medalhas de ouro, prata e bronze. 
# Considere que cada medalha de ouro tem peso 3, cada prata tem peso 2 e cada bronze peso 1.

pais_um = str(input("Digite o nome do primeiro país: "))
medalha_ouro1 = int(input("Quantas medalhas de ouro esse país recebeu? "))
medalha_prata1 = int(input("Quantas medalhas de prata esse país recebeu? "))
medalha_bronze1 = int(input("Quantas medalhas de bronze esse país recebeu? "))
pont1 = (medalha_ouro1*3)+(medalha_prata1*2)+(medalha_bronze1*1)

pais_dois = str(input("Digite o nome do segundo país: "))
medalha_ouro2 = int(input("Quantas medalhas de ouro esse país recebeu? "))
medalha_prata2 = int(input("Quantas medalhas de prata esse país recebeu? "))
medalha_bronze2 = int(input("Quantas medalhas de bronze esse país recebeu? "))
pont2 = (medalha_ouro2*3)+(medalha_prata2*2)+(medalha_bronze2*1)

pais_tres = str(input("Digite o nome do terceiro país: "))
medalha_ouro3 = int(input("Quantas medalhas de ouro esse país recebeu? "))
medalha_prata3 = int(input("Quantas medalhas de prata esse país recebeu? "))
medalha_bronze3 = int(input("Quantas medalhas de bronze esse país recebeu? "))
pont3 = (medalha_ouro3*3)+(medalha_prata3*2)+(medalha_bronze3*1)

if pont1 > (pont2 or pont3):
  if pont2 > pont3:
    print(f"primeiro:{pais_um}, segundo: {pais_dois} e terceiro: {pais_tres}.")
  else:
    print(f"primeiro:{pais_um}, segundo: {pais_tres} e terceiro: {pais_dois}.")
elif pont2 > (pont1 or pont3):
  if pont1 > pont3:
    print(f"primeiro:{pais_dois}, segundo: {pais_um} e terceiro: {pais_tres}.")
  else:
    print(f"primeiro:{pais_dois}, segundo: {pais_tres} e terceiro: {pais_um}.")
elif pont3 > (pont1 or pont2):
  if pont1 > pont2:
    print(f"primeiro:{pais_tres}, segundo: {pais_um} e terceiro: {pais_dois}.")
  else:
    print(f"primeiro:{pais_tres}, segundo: {pais_dois} e terceiro: {pais_um}.")
else: 
  print("houve empate!")
