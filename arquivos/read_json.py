import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1 = json.loads(d1_json)  # transformar para dicionário
    
for k, v in d1.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)