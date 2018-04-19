from tipoToken import TipoToken

class Token:
    def __init__(self, tipo, lexema, indice=None): 
        self.tipoToken = tipo
        self.lexema = lexema
        self.indice = indice
    
    def toString(self):
        strTipo = str(self.tipoToken)
        if self.indice != None:
            return "<"+strTipo.split('.')[1]+","+self.lexema+","+self.indice+">"
        else:
            return "<"+strTipo.split('.')[1]+","+self.lexema+">"
    
    def getTipo(self):
        return self.tipoToken
    
    def getLexema(self):
        return self.lexema
    
    def getToken(self):
        print(self.tipoToken)
        print(TipoToken[self.tipoToken])
        print(TipoToken[self.tipoToken].value)

# if __name__ == "__main__":
#     token = Token("PCChar", "if")
#     print (token.toString())
