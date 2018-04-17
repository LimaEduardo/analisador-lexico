import sys
from pathlib import Path

class LeitorDeArquivos:
    def __init__ (self, nomeArquivo):
        arquivo = Path(nomeArquivo)
        if arquivo.exists():
            self.arquivo = open(nomeArquivo, "r")
        else:
            print("Não existe")
            sys.exit()
    
    def leProximoChar(self):
        c = self.arquivo.read(1)
        if not c:
            print("O arquivo acabou!")
            return None
        print(c)
        return c

if __name__ == "__main__":
    leitor = LeitorDeArquivos("exemplo.jmm")
    leitor.leProximoChar()