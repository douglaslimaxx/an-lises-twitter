import pandas as pd

dados = pd.read_csv("./dados/base-tcc.csv")

size = len(dados["Texto"])

vocabulario = ["deus", "conservador", "pais", "direita", "tudo", "politica", "corruptos", "contra", "vida", "brasil",
               "ser", "aqui", "brasileiro", "federal", "politicamente", "carioca", "palmeirense", "esquerda", "bolsonaro",
               "verdade", "gosto", "familia", "casado", "homem", "fa", "futebol", "ladroes", "lixos", "lula", "orgulho",
               "pai", "politicos", "professor", "pt", "todos", "torcedor", "amo"]

rotulagemd = []

print(dados.columns)

for d in dados["UserDescription"].tolist():
    rotulo = 0
    if(isinstance(d, str)):
        for p in vocabulario:
            if(p in d.lower()):
                rotulo += 1
    rotulagemd.append(rotulo)

dados["rotulage-description"] = rotulagemd

dados.to_csv("./base-tcc.csv", index=False)
