from leitorDeArquivos import LeitorDeArquivos
from token import Token
from tipoToken import TipoToken
from analisadorLexico import AnalisadorLexico

if __name__ == "__main__":
    analisador = AnalisadorLexico("exemplo2.jmm")
    analisador.analisa()
    analisador.imprimeFluxoDeTokens()
    analisador.imprimeTabelaDeSimbolos()
