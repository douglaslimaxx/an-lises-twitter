import pandas as pd

dados = pd.read_csv("./dados/com-rotualgem.csv")

size = len(dados["id"])

# "r" não rotulado
# "yes" tweet homofóbico
# "no" tweet não homofóbico

if("rotulagem" in dados):
    rotulagem = dados["rotulagem"].to_list()
else:
    rotulagem = ["r"] * size

index = 0

for r in range(len(rotulagem)):
    # print(index)
    if(rotulagem[r] == "r"):
        # print(index)
        index = r
        break

print("\n O número de tweets já rolutados é %i \n" % index)

for i in range(index, size):
    # print(rotulagem)
    print("\n Tweet: %s \n (y)yes/(n)no? " % dados["Texto"][i])
    avaliacao = input()
    if(avaliacao == "y"):
        rotulagem[i] = "yes"
    elif(avaliacao == "n"):
        rotulagem[i] = "no"
    else:
        break

dados["rotulagem"] = rotulagem

dados.to_csv("./dados/com-rotualgem.csv", index=False)
