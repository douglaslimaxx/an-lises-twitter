import pandas as pd

palavra = input()

dados = pd.read_csv("./word-"+palavra+".csv")

tweets = dados["Text"]

rts = 0

for t in tweets:
    if("http" in t.lower()):
        rts += 1

print("Número de RTs foi %i" % rts)
