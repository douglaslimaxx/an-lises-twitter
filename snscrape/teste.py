with open('douglas.txt', 'r', encoding='utf-8') as arquivo:
  texto = arquivo.read()

tweets_list = texto.split("-\n")

print(tweets_list)

