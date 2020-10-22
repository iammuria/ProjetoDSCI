from flask import Flask
from prjSensores import Variaveis
from prjPandas import VariaveisDAO
from json import JSONEncoder

app = Flask(__name__)

var = Variaveis()
saveVar = VariaveisDAO()

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
    saveVar.create(var)
    return var.getAll()
        
app.run(port='8000', host='192.168.100.84')
