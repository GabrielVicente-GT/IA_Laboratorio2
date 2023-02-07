from node import *

class Network():
    def __init__(self, path):
        self.results = {}
        
        #Separación de final y creación de diccionario llave: Símbolos, valor: Probabilidad
        with open(path) as red:
            for line in red:
                line = line.strip()
                Pvalue = line.replace(" ","").split("=")
                Values = float(Pvalue[1])
                Elements = Pvalue[0].replace("P(","").replace(")","")
                self.results[Elements] = Values

    
    
# Pruebas
fileL = 'red_4.txt'
obj = Network(fileL)
print(obj.results)