with open('tweets_homofobico2.txt', 'r', encoding='utf-8') as arquivo:
  texto = arquivo.read()

tweets_list = texto.split("Idioma: pt")

print(tweets_list)

