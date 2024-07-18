import pandas as pd

dados_fiscais = pd.read_csv("dados_fiscais.csv")

parametro1 = ...
parametro2 = ...

dados_fiscais["provisao_fiscal"] = dados_fiscais["valor"] * parametro1 + parametro2

dados_fiscais.to_csv("dados_fiscais_parametrizados.csv", index=False)
