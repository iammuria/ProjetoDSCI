# Código para salvar os dados de leitura dos sensores(hora, temperatura, luminosidade, presença (0 -> vazio | 1 -> há alguém))
# Autora: Múria Viana
# Disciplina de Desenvolvimento de Sistemas Computacionais I | Sandeco
from prjClass import Variaveis
from datetime import datetime
import pandas

class VariaveisDAO():
    
    def open(self):
        df = pandas.read_csv("variaveis.csv")
        return df
    
    def save(self, df):
        df.to_csv("variaveis.csv", index = False)
    
    def create(self, var):
        df = self.open()
        
        new_id = self.get_new_id(df)
        var.id = new_id
        
        hour = datetime.now()
        hour = hour.strftime('%H:%M:%S')
        var.hora = hour
        
        new_row = pandas.DataFrame(data=[[
                                    new_id, hour, var.temp, var.lumi, var.pres
                                    ]],
                                    columns = df.columns)
        df = df.append(new_row)
        
        self.save(df)
        
    def get_new_id(self, df):
        if len(df) == 0:
            id = 1
        else:
            last = df.tail(1)
            id = last.id.values[0] + 1
            
        return id
    
    
    '''def read(self,id):

        df = self.open()
        i = self.get_index(id, df)

        var = Variaveis()

        var.id = id
        var.hora = df.iloc[i].hour
        var.temp = df.iloc[i].temp
        var.lumi = df.iloc[i].lumi
        var.pres = df.iloc[i].pres

        return var


    def read_all(self):

        df = self.open()

        vars = []


        for i in range(len(df)):
            var = Variaveis()
            var.id = df.iloc[i].id
            var.hora = df.iloc[i].hour
            var.temp = df.iloc[i].temp
            var.lumi = df.iloc[i].lumi
            var.pres = df.iloc[i].pres

            vars.append(var)

        return var'''

    def delete(self):
        df = self.open()
        tam = len(df)
        i = 1
        while i <= tam:
            df = self.open()
            index = self.get_index(i,df)
            df = df.drop(index)
        
            self.save(df)
            
            i += 1
        df.reset_index(drop = True, inplace = True)
        
    def get_index(self, id, df):

        index = df.loc[df.id == id, :].index[0]

        return index
