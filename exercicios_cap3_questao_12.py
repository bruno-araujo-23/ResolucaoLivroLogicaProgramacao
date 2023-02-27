# Construa um algoritmo capaz de concluir qual dentre os seguintes animais foi escolhido
# através de perguntas e respostas. Animais possíveis: leao, cavalo, homem, macaco, morcego
# baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.

# perguntas
vertebrado = int(input("O animal é 1- mamífero / 2- ave / 3- reptil? - resposta: "))

if vertebrado == 1:
  locomocao = int(input("O animal é 1- quadrúpede / 2- bípede / 3- voador / 4- aquático? - resposta: "))
  if locomocao == 1:
    alimentacao = int(input("O animal é 1- carnívoro / 2- herbívoro? - resposta: "))
    if alimentacao == 1:
      print("o animal é um leão.")
    elif alimentacao == 2:
      print("o animal é um cavalo.")
    else:
      print("digite uma opção válida")
  elif locomocao == 2:
    alimentacao2 = int(input("o animal é 1- onívoro / 2- frutívoro? - resposta: "))
    if alimentacao2 == 1:
      print("o animal é um homem.")
    elif alimentacao2 == 2:
      print("o animal é um macacao.")
    else:
      print("digite uma opção válida")
  elif locomocao == 3:
    print("o animal é um morcego.")
  elif locomocao == 4:
    print("o animal é uma baleia.")
  else:
    print("digite uma opção válida.")
elif vertebrado == 2:
  tipo_ave = int(input("A ave é 1- não voadora / 2- nadadora / 3- rapina? - resposta: "))
  if tipo_ave == 1:
    clima_ave = int(input("A ave vive em área 1- tropical / 2- polar? - resposta: "))
    if clima_ave == 1:
      print("o animal é um avestruz.")
    elif clima_ave == 2:
      print("o animal é um pinguim.")
    else:
      print("digite uma opção válida.")
  elif tipo_ave == 2:
    print("o animal é um pato.")
  elif tipo_ave == 3:
    print("o animal é uma águia.")
  else:
    print("digite uma opção válida.")
elif vertebrado == 3:
  tipo_reptil = int(input("O réptil é 1- com casco / 2- carnívoro / 3- sem pata? - resposta: "))
  if tipo_reptil == 1:
    print("o animal é uma tartaruga.")
  elif tipo_reptil == 2:
    print("o animal é um crocodilo.")
  elif tipo_reptil == 3:
    print("o animal é uma cobra.")
  else:
    print("digite uma opção válida.")
else:
  print("digite uma opção válida.")
