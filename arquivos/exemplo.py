import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Ana',
        'idade': 21,
    },
}

d1_json = json.dumps(d1, indent=True)  # transforma o dicionário para json
# print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
