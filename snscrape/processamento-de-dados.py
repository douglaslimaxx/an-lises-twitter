# coding utf-8
import pandas as pd


def remover_mencao(tweet: str):
    toReturn = []
    lista = tweet.split()
    for termo in lista:
        if not(("@" in termo) or ("http" in termo)):
            toReturn.append(termo)
    return " ".join(toReturn)


dados = pd.read_csv("./base-dados.csv")

limpo = []

for t in dados["Texto"]:
    limpo.append(remover_mencao(t))

dados["Texto-Limpo"] = limpo

dados.to_csv("./dados-limpos.csv")
