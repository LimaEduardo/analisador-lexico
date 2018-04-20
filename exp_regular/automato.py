# Le um arquivo de palavras separadas pro quebra de linha
# cria uma saida em um arquivo chamado "SaidaAutomato" com todas letras em sequencia
# de cada palavra ja gerando um arquivo pronto para o uso no GRAPHVIZ

from pathlib import Path

def geraGrafo(p1, p2, label):
    return "    " + p1 + " -> " + p2 +" [ label = " +label+ " ]"; 

if __name__ == "__main__":
    inicial = "q0"
    arquivo = Path("ex.txt")
    linhasArquivo = []

    if arquivo.exists():
        arquivo = open("ex.txt", "r")
        linhasArquivo = arquivo.read().split()
        arquivo.close()
    else:
        print("Não existe")
        sys.exit()

    lexemas = []
    for linha in linhasArquivo:
        lexemas.append(list(linha))
    indice = 1
    q0 = {}
    indPalavra = 0
    
    arq = open("saidaAutomato",'w')
    arq.write("digraph\n{\n    rankdir = LR\n")
    while indPalavra < len(lexemas):
        q0['q' + str(indice)] = lexemas[indPalavra][0]
        indCaractere = 1
        arq.write("\n")
        while indCaractere < len(lexemas[indPalavra]):
            arq.write(geraGrafo('q'+str(indice), 'q'+str(indice + 1), lexemas[indPalavra][indCaractere]) + "\n")
            indice += 1
            indCaractere += 1
        indPalavra += 1
        indice += 1
    
    for value in q0:
        arq.write(geraGrafo('q0', value, q0[value]) + "\n")
    arq.write("}")
    arq.close
