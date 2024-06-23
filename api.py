import json
import requests
import pandas as pd
p = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados/ultimos/10?formato=json')
response = p.json()
# print(type(response))
result = json.dumps(response, indent=4, sort_keys=False)
# print(result)
df = pd.read_json(result)
df1 = df.to_string()
# print(df)
with open('sample.txt', 'w')as file:
     file.write(df1)
file = open('sample.txt', 'r')
print(file.read())

print ("Mumbai")
