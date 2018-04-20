import sys

class Error:
    def __init__ (self,linha,inicioLexema,linhasArquivo,operadores, separadores, tipo= None,mensagem=None):
        tiposDisponiveis = ['lexico','sintatico','semantico']
        fimLexema = inicioLexema
        
        while (not self.acabouLexema(linhasArquivo, linha, fimLexema, operadores, separadores)):
            fimLexema += 1
        
        lex = linhasArquivo [linha][inicioLexema:fimLexema]
        
        if tipo in tiposDisponiveis:
            print("Erro "+tipo+" encontrado na linha "+str(linha+1)+" e na coluna "+str(inicioLexema))
            print(lex)
        else:
            print ("Erro encontrado na linha "+str(linha+1)+" e na coluna "+str(inicioLexema))
            print(lex)

        if mensagem != None:
            print (mensagem) 
        
    def acabouLexema(self, linhas, linha, indice, operadores, separadores):
        especiais = [' ', '\t']
        if(linhas[linha][indice] in operadores or linhas[linha][indice] in separadores or linhas[linha][indice] in especiais):
            return True
        if(indice < len(linhas[linha]) - 1):
            t = linhas[linha][indice:indice + 2]
            if t in operadores:
                return True
        return False
            
        
            
  
