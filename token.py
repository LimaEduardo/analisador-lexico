from tipoToken import TipoToken

class Token:
    def __init__(self, tipo, lexema, indice=None): 
        self.tipoToken = tipo
        self.lexema = lexema
        if indice is not None:
            self.indice = indice
        else: 
            self.indice = indice
    
    def toString(self):
        if self.indice != None:
            return "<"+str(TipoToken[self.tipoToken].name)+","+self.lexema+","+self.indice+">"
        else:
            return "<"+str(TipoToken[self.tipoToken].value[1])+","+self.lexema+">"
    
    def getToken(self):
        print(self.tipoToken)
        print(TipoToken[self.tipoToken])
        print(TipoToken[self.tipoToken].value)

if __name__ == "__main__":
    token = Token("PCChar", "if")
    print (token.toString())
