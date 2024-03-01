# fazer requisiçoes 
import requests

#para criar uma pagina na web
from flask import *

import pprint

print('qual é seu cep: ?\n')
cep_client = input(str())

# retirando os espaços no começo e no fim da string
cep_client = cep_client.strip()

if len(cep_client) == 9:
    cep_client = cep_client.replace('-', "")

r = requests.get(f"https://viacep.com.br/ws/{cep_client}/json")
r = r.json()


app = Flask(__name__)


# $ set FLASK_APP=main.py
# $ run FLASK
@app.get('/')
def return_cep():
    return r