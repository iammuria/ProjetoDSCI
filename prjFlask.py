from flask import Flask
from prjClass import Variaveis

from json import JSONEncoder

app = Flask(__name__)

var = Variaveis(0, 0, 1)

@app.route("/")
def saudacoes():
    return "Projeto da Múria"


@app.route("/definir-medidas/<temp>/<lumi>")
def definir(temp, lumi):
    
    temp = int(temp)
    lumi = int(lumi)
    
    var.setTemp(temp)
    var.setLumi(lumi)

    return "Concluido"

@app.route("/ler-medidas/")
def ler():
    return var.getAll()
        
app.run(port='8000', host='192.168.100.84')