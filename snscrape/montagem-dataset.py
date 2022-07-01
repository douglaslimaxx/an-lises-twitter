import pandas as pd

dados = pd.read_csv("./dados/base-tcc.csv")

del dados["id"]

dados.rename(columns={"Unnamed: 0.3": "id"}, inplace=True)

# del dados["Unnamed: 0.2"]
# del dados["Unnamed: 0.1"]
# dados["id"] = dados["Unnamed: 0"]
# del dados["Unnamed: 0"]

# del dados["Retweet"]
# del dados["Quoted"]
# del dados["rotulagem-manual"]

print(len(dados["Texto"]))

# hatespeech = []

# for t in dados["HateSpeech"].tolist():
#     if(t == "yes"):
#         hatespeech.append(1)
#     else:
#         hatespeech.append(0)

# homofobia = []

# for h in dados["rotulagem"].tolist():
#     if(t == "yes"):
#         homofobia.append(1)
#     else:
#         homofobia.append(0)

# dados["HateSpeechC"] = hatespeech

# dados["rotulagem-homofobia"] = homofobia

dados.to_csv("./dados/base-tcc.csv", index=False)
