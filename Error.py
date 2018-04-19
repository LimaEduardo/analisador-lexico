class Error:
    def __init__ (self,linha,coluna,tipo= None,mensagem=None):
        tiposDisponiveis = ['lexico','sintatico','semantico']
        if tipo in tiposDisponiveis:
            print("Erro "+tipo+" encontrado na linha "+linha+" e na coluna "+coluna)
            print (mensagem) if mensagem not None
        else:
            print ("Erro encontrado na linha "+linha+" e na coluna "+coluna)
            print (mensagem) if mensagem not None
            
  