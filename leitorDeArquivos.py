import sys
from pathlib import Path

class LeitorDeArquivos:
    def __init__ (self, nomeArquivo):
        self.arquivo = Path(nomeArquivo)
        self.linha = 0
        self.coluna = 0

        if self.arquivo.exists():
            self.arquivo = open(nomeArquivo, "r")
        else:
            print("Não existe")
            sys.exit()
    
    def leProximoChar(self):
        c = self.arquivo.read(1)
        self.coluna += 1
        if c == "\n":
            self.linha += 1
            self.coluna = 0
        if not c:
            print("O arquivo acabou!")
            return None
        print(c, self.linha, self.coluna)
        return c
    
    def getLinhaColuna(self):
        return [self.linha,self.coluna]

# if __name__ == "__main__":
#     leitor = LeitorDeArquivos("exemplo.jmm")
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()
#     leitor.leProximoChar()