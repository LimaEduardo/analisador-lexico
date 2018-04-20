import sys

class Error:
    def __init__ (self,linha,coluna,tipo= None,mensagem=None):
        tiposDisponiveis = ['lexico','sintatico','semantico']
        if tipo in tiposDisponiveis:
            print("Erro "+tipo+" encontrado na linha "+str(linha+1)+" e na coluna "+str(coluna))
        else:
            print ("Erro encontrado na linha "+str(linha+1)+" e na coluna "+str(coluna))

        if mensagem != None:
            print (mensagem) 
        
            
  
