import pandas as pd

# palavra = input()

# dados = pd.read_csv("../../dados-tcc/word-"+palavra+".csv")

# dados = pd.read_csv("./dados/dados-finalizadocs.csv")
# dados = pd.read_csv("./dados/base-tcc.csv")
dados = pd.read_csv("./dados/montados.csv")

# toxidade = dados["toxidade"]
# hate = dados["HateSpeech"]
# palavras = dados["Palavra"].to_list()

tweets = dados["Texto"].to_list()
rotulagem = dados["rotulagem"].to_list()

# print(len(palavras))

termos = ["baitola", "bichona", "bixa", "boiola", "gayzada",
          "gayzismo", "homossexualismo", "viadagem", "viadao", "viadinho", "bicha", "viado"]

c = 0
h = 0
n = 0
for i in range(len(tweets)):
    if('viado' in tweets[i].split()):
        c += 1
        if(rotulagem[i] == "yes"):
            h += 1
        else :
            n +=1
print("Foram %i tweets com a palavra %s" % (c, 'viado'))
print("Foram %i tweets homofobicos com a palavra %s" % (h, 'viado'))
print("Foram %i tweets não homofóbicos com a palavra %s" % (n, 'viado'))

# toxic_hate = 0
# is_hate_notToxic = 0

# for t in range(len(toxidade)):
#     if(toxidade[t] == 1):
#         toxic_hate += 1
#     if(hate[t] == "yes"):
#         is_hate_notToxic += 1

# print("O número de tweets tóxicos foi %i" % toxic_hate)
# print("O número de tweets com discurso de ódio foi %i" %
#       is_hate_notToxic)

# del dados["Unnamed: 0.2"]

# del dados["Unnamed: 0.1"]
# del dados["Unnamed: 0.1.1"]

# dados.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

# dados["rotulagem-manual"] = None

# dados.to_csv("./dados-finalizados.csv", index=False)

# print(dados.columns)

# toxidade = dados["toxidade"]
# hate = dados["HateSpeech"]
# rotulagem = dados["Rotulagem"]
# tweets_ids = dados["TweetId"]
# tweets_ids_r = dados_r["TweetId"]

# size = len(rotulagem)
# print(size)
# homofobico = 0

# ids = []

# for i in range(size):
#     if(hate[i] == "yes" and rotulagem[i] == "yes"):
#         ids.append(tweets_ids[i])
#         homofobico += 1

# print({"homo-hate": homofobico})

# rotulados = 0

# for t in ids:
#     if(t in tweets_ids_r.to_list()):
#         rotulados += 1

# print({"rotulados": rotulados})


# dados = pd.read_csv("./dados/dados-finalizados.csv")

# palavras = ["baitola", "bichona", "bixa", "boiola", "gayzada",
#             "gayzismo", "homossexualismo", "viadagem", "viadao", "viadinho", "bicha"]

# tweets = dados["Texto"]
# print(len(tweets))

# duplicated = 0

# for t in tweets:
#     check_p = 0
#     for p in palavras:
#         if(p in t):
#             check_p += 1
#     if(check_p == 0):
#         duplicated += 1

# print(duplicated)
