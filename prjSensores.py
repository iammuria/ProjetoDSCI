from prjClass import Variaveis

if __name__ == '__main__':
    var = Variaveis(35, 30, 0)
    var.printAll()
    
    var.setTemp(24)
    var.setLumi(50)
    var.setPres(1)
    print(var.printAll())