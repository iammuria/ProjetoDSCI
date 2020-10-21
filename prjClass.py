import json 
class Variaveis():

    def __init__(self, temp=0, lumi = 0, pres = 0):
        self.id = None
        self.temp = temp
        self.lumi = lumi
        self.pres = pres
    
    def getTemp(self):
        return self.temp

    def setTemp(self, temp):
        self.temp = temp

    def getLumi(self):
        return self.lumi

    def setLumi(self, lumi):
        self.lumi = lumi

    def getPres(self):
        return self.pres
        
    def setPres(self, pres):
        if pres == 0 | pres == 1:
            self.pres = pres
        else:
            return "valor inválido"
    
    def getAll (self):
        all = {
            "temp" : self.temp,
            "lumi" : self.lumi,
            "pres" : self.pres
        }
        res = json.dumps(all)
        return  res
    
    def printAll(self):
        if self.pres == 0:
            return f'Temperatura: {self.temp} ºC  ' + f'Luminosidade: {self.lumi} %  ' + 'A sala está vazia'
        else:
            return f'Temperatura: {self.temp} ºC  ' + f'Luminosidade: {self.lumi} %  ' + 'Há alguém na sala'           