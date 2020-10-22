from modules.fb import login
import json

with open('contas.json', 'r') as dadosContas:
    data = dadosContas.read()

contas = json.loads(data)

for conta in contas:
    login.login(conta)
