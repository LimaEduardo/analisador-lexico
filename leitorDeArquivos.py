import sys
from pathlib import Path

class LeitorDeArquivos:
    def __init__ (self, nomeArquivo):
        arquivo = Path(nomeArquivo)
        self.linhasArquivo = []
        self.linha = 0
        self.coluna = 0
        self.indice = 0

        if arquivo.exists():
            arquivo = open(nomeArquivo, "r")
            self.linhasArquivo = arquivo.read().splitlines()
            arquivo.close()
        else:
            print("Arquivo nao existe")
            sys.exit()
    
    # def leProximoChar(self):
    #     c = self.arquivo.read(1)
    #     self.coluna += 1
    #     if c == "\n":
    #         self.linha += 1
    #         self.coluna = 0
    #     if not c:
    #         print("O arquivo acabou!")
    #         return None
    #     print(c, self.linha, self.coluna)
    #     self.indice 
    #     return c
    
    # def getLinhaColuna(self):
    #     return [self.linha,self.coluna]

if __name__ == "__main__":
    leitor = LeitorDeArquivos("exemplo.jmm")
