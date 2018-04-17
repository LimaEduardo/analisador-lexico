from leitorDeArquivos import LeitorDeArquivos
from token import Token
from tipoToken import TipoToken
from analisadorLexico import AnalisadorLexico

if __name__ == "__main__":
    analisador = AnalisadorLexico("exemplo.jmm")
    token = None
    while token = analisador.proximoToken() != None:
        print(token)