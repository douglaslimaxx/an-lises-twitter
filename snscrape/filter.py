import pandas as pd

dados = pd.read_csv("./dados/dados-finalizados.csv")

filtrados = dados[dados["HateSpeech"] == "yes"]

filtrados.to_csv("./filtrados.csv")
