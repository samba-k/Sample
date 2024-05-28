import pandas as pd
df = pd.read_csv("tsv.txt", sep="\s")
df.to_csv('tsv,txt',header=df.columns, index=None, sep=' ')
print(df.loc[1:3])
df.replace(1.4, None, inplace = True)
print(df)
df.dropna(inplace=True)
print(df)
