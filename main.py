from leitorDeArquivos import LeitorDeArquivos
from token import Token
from tipoToken import TipoToken
from analisadorLexico import AnalisadorLexico
import sys

if __name__ == "__main__":
    input_file_name = ""
    if len(sys.argv) == 2:
        nomeArquivoEntrada = sys.argv[1]
    else:
        print("Número inválido de argumentos. Informe o arquivo de entrada")
        sys.exit()
    analisador = AnalisadorLexico(nomeArquivoEntrada)
    analisador.analisa()
    analisador.imprimeFluxoDeTokens()
    analisador.imprimeTabelaDeSimbolos()
