from prjClass import Variaveis
import pandas
# C - Create
# R - Read/ReadAll
# U - Update
# D - Delete
#Vou fazer: Create / ReadAll / DeleteAll
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
        
        new_row = pandas.DataFrame(data=[[
                                    new_id, var.temp, var.lumi, var.pres
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
    
###############################################################################
    
    def read(self,id):

        df = self.open()
        i = self.get_index(id, df)

        var = Variaveis()

        var.id = id
        var.temp = df.iloc[i].temp
        var.lumi = df.iloc[i].lumi
        var.pres = df.iloc[i].pres

        return var


    def read_all(self):

        df = self.open()

        var = []


        for i in range(len(df)):
            var = Variaveis()
            var.id = df.iloc[i].id
            var.temp = df.iloc[i].temp
            var.lumi = df.iloc[i].lumi
            var.pres = df.iloc[i].pres

            var.append(var)

        return var

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

    def get_index(self, id, df):

        index = df.loc[df.id == id, :].index[0]

        return index

###############################################################################

if __name__ == '__main__':
    variaveis = Variaveis(20,100,1)
    
    dao = VariaveisDAO()
    dao.create(variaveis)
        
    variaveis.setTemp(25)
    variaveis.setLumi(50)
    variaveis.setPres(0)
    
    dao = VariaveisDAO()
    
    dao.create(variaveis)
    
    print(dao.open())
    
    dao.delete()
    
    print(dao.open())
    