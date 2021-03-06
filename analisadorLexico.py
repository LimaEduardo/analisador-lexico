import re

from leitorDeArquivos import LeitorDeArquivos
from prettytable import PrettyTable
from tipoToken import TipoToken
from token import Token
from error import Error

class AnalisadorLexico:

    def __init__(self, nomeArquivoEntrada):
        self.arquivo = LeitorDeArquivos(nomeArquivoEntrada)
        self.arquivoLinhas = self.arquivo.linhasArquivo
        self.fluxoDeTokens = []
        self.tabelaDeSimbolos = {}
                        #Operadores:  = == > ++ && <= ! - -- + += *
        self.operador = {"=": TipoToken.OPRecebe , "==" : TipoToken.OPIgual, ">": TipoToken.OPMaior, "++" : TipoToken.OPIncrementa, "&&" : TipoToken.OPAnd, "<=" : TipoToken.OPMenorIgual, "!" : TipoToken.OPNao, "-" : TipoToken.OPMenos, "--" : TipoToken.OPDecrementa, "+" : TipoToken.OPSoma, "+=" : TipoToken.OPSomaERecebe, "*": TipoToken.OpMultiplica }
        self.separador = {",": TipoToken.SepVirgula, "." : TipoToken.SepPonto, "[" : TipoToken.SepAbreColchete, "{" : TipoToken.SepAbreChave, "(" : TipoToken.SepAbreParentese, ")" : TipoToken.SepFechaParentese,"}" : TipoToken.SepFechaChave, "]" : TipoToken.SepFechaColchete, ";" : TipoToken.SepPontoEVirgula}
        self.reservada = {"abstract": TipoToken.PCAbstract, "boolean" : TipoToken.PCBoolean, "char" : TipoToken.PCChar, "class" : TipoToken.PCClass, "else" : TipoToken.PCElse ,"extends" : TipoToken.PCExtends ,"false" : TipoToken.PCFalse, "import" : TipoToken.PCImport, "if": TipoToken.PCIf ,"instanceof" : TipoToken.PCInstanceOf, "int" : TipoToken.PCInt, "new" : TipoToken.PCNew, "null" : TipoToken.PCNull, "package" : TipoToken.PCPackage, "private" : TipoToken.PCPrivate, "protected": TipoToken.PCProtected ,"public" : TipoToken.PCPublic, "return" : TipoToken.PCReturn, "static" : TipoToken.PCStatic, "super" : TipoToken.PCSuper, "this" : TipoToken.PCThis, "true" : TipoToken.PCTrue, "void" : TipoToken.PCVoid, "while" : TipoToken.PCWhile}
        self.literal = {"int_literal": TipoToken.Int, "char_literal": TipoToken.Char, "string_literal": TipoToken.String, "variavel_literal": TipoToken.Variavel}
        self.caracteresDaLinguagem = self.listaCaracteres()
        self.comentario = False
        self.string = False
    
    def listaCaracteres(self):
        lista = []
        for i in range(ord('a'),ord('z') + 1):
            lista.append(chr(i))
        for i in range(ord('A'),ord('Z') + 1):
            lista.append(chr(i))
        for i in range(0,10):
            lista.append(i)
            lista.append(str(i))
        for operador in self.operador:
            lista.append(operador)
        for separador in self.separador:
            lista.append(separador)
        especiais = ['_','$', '\n', '\r', '\t','\b','\f','\'', '"','\\',' ']
        for especial in especiais:
            lista.append(especial)
        return lista
    
    
    def ehCharIdentificador(self,c):
        if ((ord('a') <= ord(c)) and (ord(c) <= ord('z'))) or ((ord('A') <= ord(c)) and (ord(c) <= ord('Z'))) or c == '_' or c == '$':
            return True
        else:
            return False
            
    def ehNumero(self,c):
        return c.isdigit()
                                        # Unitario:  = > ! - + * 
    def possivelOperador(self, c):      # Dup     :  == ++ += && <= --
        if c == '&' or c == '<' or c in self.operador:
            return True
        else:
            return False
            
    def possivelIdentificador(self, c):
        if (self.ehCharIdentificador(c)) or (self.ehNumero(c)) or (c == '_') or (c == '$'):
            return True
        else:
            return False
    
    def ehIndiceValidoCol(self,indiceLin, indiceCol):
        if indiceCol < len(self.arquivoLinhas[indiceLin]):
            return True
        else:
            return False
    
    def analisa(self):
        iniLexema = 0
        indiceLinha = 0
        while (indiceLinha < len(self.arquivoLinhas)):
            indiceColuna = 0
            while (indiceColuna < len(self.arquivoLinhas[indiceLinha])):
                caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                
                #-------------------------------------------------------------
                # Testa se é um comentario
                if caractere == '/':
                    if self.ehIndiceValidoCol(indiceLinha, indiceColuna+1):
                        c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                        if c1 == '/':
                            #Então é um comentário
                            indiceLinha += 1
                            indiceColuna = 0
                            continue
                #-------------------------------------------------------------
                
                #-------------------------------------------------------------
                # Testa se é uma string Literal (v)
                
                # Verifica se o primeiro char é uma aspas duplas
                if caractere == '"':
                    #guarda os indices iniciais
                    indiceIniColuna = indiceColuna
                    indiceIniLinha = indiceLinha
                    
                    #Se o proximo indice for válido, ande nele.
                    # Se não, provavelmente chegou em um fim de linha, então vá para a proxima linha
                    if self.ehIndiceValidoCol(indiceLinha, indiceColuna+1):
                        indiceColuna += 1
                        c = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                    else:
                        indiceLinha += 1
                        indiceColuna = 0
                        c = self.arquivoLinhas[indiceLinha][indiceColuna]
                        
                    #Enquanto não achar outras aspas duplas (fechamento) percorra
                    while c != '"':
                        #Se o proximo indice é valido, ande no arquivo
                        #Se o proximo indice não é valido, pule a linha
                        if self.ehIndiceValidoCol(indiceLinha, indiceColuna):
                            c = self.arquivoLinhas[indiceLinha][indiceColuna]
                        else:
                            indiceColuna = 0
                            indiceLinha += 1
                            c = self.arquivoLinhas[indiceLinha][indiceColuna]
                        indiceColuna += 1
                    #Inicio da montagem do lexema
                    lexema = ""
                    # guarda os indices finais
                    indiceFinalColuna = indiceColuna
                    indiceFinalLinha = indiceLinha
                    
                    #Se o indice final é igual ao inicial, quer dizer que a string está em uma só linha
                    if indiceIniLinha == indiceFinalLinha:
                        lexema = self.arquivoLinhas[indiceFinalLinha][indiceIniColuna: indiceFinalColuna]
                        self.geraToken(self.literal["string_literal"], lexema, indiceFinalLinha, indiceFinalColuna)
                        continue
                    
                    error = Error(indiceLinha, indiceColuna, "lexico",  "Quebra de linha dentro de uma string")
                    
                    #Se chegar aqui, é pq é uma string multilinhas
                    '''for linha in range(indiceIniLinha, indiceFinalLinha+1):
                        #Se é a primeira linha, pega da coluna inicial até o final da linha
                        if(linha == indiceIniLinha):
                            lexema += self.arquivoLinhas[linha][indiceIniColuna: len(self.arquivoLinhas[linha])]
                        #Se é a ultima linha, pega da coluna 0 até a coluna final
                        elif (linha == indiceFinalLinha):
                            lexema += self.arquivoLinhas[linha][0: indiceFinalColuna]
                        #Se não é final nem inicial, pega a linha toda
                        else:
                            lexema += str(self.arquivoLinhas[linha])
                    lexema = re.sub(' +',' ',lexema) #Expressão regular para tirar excesso de espaços
                    self.geraToken(self.literal["string_literal"], lexema)
                    continue'''
                    
                        
                        
                #-------------------------------------------------------------
                
                
                
                #-------------------------------------------------------------
                # Testa se é um char Literal (v)
                
                #if not ehCharLiteral and caractere == '\'':
                if caractere == '\'':
                    if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 1):
                        c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                        if c1 == '\\':
                            if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 2):
                                c2 = self.arquivoLinhas[indiceLinha][indiceColuna + 2]
                                if  c2 == 'n' or c2 == 'r' or c2 == 't' or c2 == 'b' or c2 == 'f' or c2 == '\'' or c2 == '\"' or c2 == '\\' :
                                    if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 3) and self.arquivoLinhas[indiceLinha][indiceColuna + 3] == '\'':
                                        self.geraToken(self.literal["char_literal"], caractere+c1+c2+c3, indiceLinha, indiceColuna + 2)
                                        indiceColuna += 3
                                        continue
                                        
                                    else: # c3 é diferente de aspas simples (')
                                        error = Error(indiceLinha, indiceColuna, "lexico", "não e char literal")
                                        
                                else: # c2 é diferente '\n' '\r' '\t' '\b' '\f' '\’' '\"' '\\'
                                    error = Error(indiceLinha, indiceColuna, "lexico", "não e char literal")
                            else:
                                error = Error(indiceLinha, indiceColuna, "lexico", "não e char literal, fim de linha")
                        elif c1 != '\'' and c1 != '\\':
                            if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 2):
                                c2 = self.arquivoLinhas[indiceLinha][indiceColuna + 2]
                                if c2 == '\'':
                                    self.geraToken(self.literal["char_literal"], caractere+c1+c2, indiceLinha, indiceColuna +1)
                                    indiceColuna += 2
                                    continue
                                    
                                else: # c2 é diferente de aspas simples (')
                                    error = Error(indiceLinha, indiceColuna, "lexico",  "não e char literal")
                                
                        else: # c1 for igual a aspas simples (') ou igual uma barra(\)
                            error = Error(indiceLinha, indiceColuna, "lexico",  "não e char literal")
                    else:
                        error = Error(indiceLinha, indiceColuna, "lexico", "não e char literal, fim de linha")
                #-------------------------------------------------------------
                
                
                
                #-------------------------------------------------------------
                # Teste se achou um identificador (v)
                if self.ehCharIdentificador(caractere):
                    iniLexema = indiceColuna
                    #~ print(caractere)
                    if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 1):
                        indiceColuna += 1
                        caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                        #~ print(caractere)
                        fimIdent = False
                        while (not fimIdent) and (self.possivelIdentificador(caractere)):
                            indiceColuna += 1
                            if self.ehIndiceValidoCol(indiceLinha, indiceColuna):
                                caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                            else:
                                fimIdent = True
                                
                    else: # Para ultilizar esse metodo [ inicio : fim ] precisa ir ate o indice invalido caso necessario
                        indiceColuna += 1
                    
                    lexema = self.arquivoLinhas[indiceLinha][iniLexema : indiceColuna]
                    
                    if lexema not in self.reservada:  
                        self.geraToken(self.literal["variavel_literal"], lexema, indiceLinha, iniLexema)
                        continue
                    else:
                        self.geraToken(self.reservada[lexema], lexema, indiceLinha, iniLexema)
                        continue
                #-------------------------------------------------------------
                
                #-------------------------------------------------------------
                # Teste se é um numero (v)
                if self.ehNumero(caractere):
                    if caractere == '0':
                        if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 1):
                            c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                            
                            if(c1 == " ") or (self.possivelOperador(c1)) or (c1 in self.separador) or (c1 == "\t"):
                                self.geraToken(self.literal["int_literal"], caractere, indiceLinha, iniLexema)
                                indiceColuna += 1
                                continue
                            elif self.ehNumero(c1) : # Caso proximo ao zero  nao seja caracter valido
                                error = Error(indiceLinha, indiceColuna, "lexico",  "Numero Invalido")
                            elif self.possivelIdentificador(c1):
                                error = Error(indiceLinha, indiceColuna, "lexico",  "Variavel Invalida")
                        else:
                            self.geraToken(self.literal["int_literal"], caractere, indiceLinha, iniLexema)
                    else:
                        iniLexema = indiceColuna
                        while caractere != None and self.ehNumero(caractere):
                            indiceColuna += 1
                            if self.ehIndiceValidoCol(indiceLinha, indiceColuna):
                                caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                            else:
                                caractere = None
                        if caractere != None and self.possivelIdentificador(caractere):
                            error = Error(indiceLinha, iniLexema, "lexico",  "Variavel Invalida")
                        else:
                            lexema = self.arquivoLinhas[indiceLinha][iniLexema:indiceColuna]
                            self.geraToken(self.literal["int_literal"], lexema, indiceLinha, iniLexema)
                            continue
                            
                #-------------------------------------------------------------



                #-------------------------------------------------------------
                # Testa se caracter é um operador (v)
                
                ehOperadorUni = False
                ehOperadorDup = False
                                                    # Unitario:  = > ! - + * 
                                                    # Dup     :  == ++ += && <= --
                if self.possivelOperador(caractere):
                    if caractere in self.operador:
                        ehOperadorUni = True
                        
                    if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 1):
                        c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1] 
                        if caractere == '=':
                            if c1 == '=':
                                ehOperadorDup = True
                                ehOperadorUni = False
                        elif caractere == '+':
                            if c1 == '+':
                                ehOperadorDup = True
                                ehOperadorUni = False
                            elif c1 == '=':
                                ehOperadorDup = True
                                ehOperadorUni = False
                        elif caractere == '&':
                            if c1 == '&':
                                ehOperadorDup = True
                                ehOperadorUni = False
                        elif caractere == '<':
                            if c1 == '=':
                                ehOperadorDup = True
                                ehOperadorUni = False
                        elif caractere == '-':
                            if c1 == '-':
                                ehOperadorDup = True
                                ehOperadorUni = False
                    
                        # Criando os tokens de um operador
                        if ehOperadorDup:
                            self.geraToken(self.operador[caractere+c1], caractere+c1, indiceLinha, indiceColuna)
                            indiceColuna += 2
                            continue
                        elif ehOperadorUni:
                            self.geraToken(self.operador[caractere], caractere, indiceLinha, indiceColuna)
                            indiceColuna += 1
                            continue
                #-------------------------------------------------------------
                
                
                #-------------------------------------------------------------
                #testa se caractere é um separador (v)
                if caractere in self.separador:
                    self.geraToken(self.separador[caractere], caractere, indiceLinha, indiceColuna)
                    indiceColuna += 1
                    continue
                #-------------------------------------------------------------
                
                
                #-------------------------------------------------------------
                # testa se é um caractere inválido (v)
                if caractere not in self.caracteresDaLinguagem:
                    error = Error(indiceLinha, indiceColuna, "lexico",  "caractere não pertence a linguagem")
                #-------------------------------------------------------------
                indiceColuna += 1
                
                
            indiceLinha += 1
    
    def separador(self, char):
        try:
            if str(TipoToken[char].value[1] == "separador"):
                return True
        except:
            return False
    
    def operador(self, char):
        try:
            if str(TipoToken[char].value[1] == "operador"):
                return True
        except:
            return False

    def geraToken(self, tipoToken, lexema, linha, coluna):
        # Se é um desses tipos, deverá ser registrado na tabela de simbolos
        if tipoToken == self.literal["int_literal"] or tipoToken == self.literal["char_literal"] or tipoToken == self.literal["string_literal"] or tipoToken == self.literal["variavel_literal"]:
            #print (lexema, tipoToken)
            # Se o lexema não existir na tabela, então insere ele
            if lexema not in self.tabelaDeSimbolos.values():
                #O indice é vai ser dado pelo tamanho atual da tabela de simbolos
                #Insere o token na tabela de simbolos, cria o token e adiciona nno fluxo de tokens
                index = len(self.tabelaDeSimbolos)
                self.tabelaDeSimbolos[index] = lexema
                token = Token(tipoToken, lexema, linha, coluna, index)
                self.fluxoDeTokens.append(token)
                return
            else:
                #Se o token já existe, precisamos então ver com é o indice dele para inserir no fluxo de tokens
                index = [chave for chave in self.tabelaDeSimbolos if self.tabelaDeSimbolos[chave] == lexema][0] # <- é gambiarra, mas funciona.
                token = Token(tipoToken, lexema, linha, coluna, index)
                self.fluxoDeTokens.append(token)
                return
        else:
            # Se o lexema não for de um tipo que requer um tipo, então é só inserir este no fluxo de tokens
            token = Token(tipoToken, lexema, linha, coluna)
            self.fluxoDeTokens.append(token)
            return
            
    def imprimeTabelaDeSimbolos(self):
        tabelaDeSimbolos = open("tabelaDeSimbolos",'w')
        t = PrettyTable(['Indice', 'Lexema'])
        for indice in self.tabelaDeSimbolos:
            t.add_row([str(indice), str(self.tabelaDeSimbolos[indice])])
            #tabelaDeSimbolos.write("|" + str(indice) + "|" + str(self.tabelaDeSimbolos[indice] + "| \n"))
        tabelaDeSimbolos.write(str(t))
        tabelaDeSimbolos.close()
    
    def imprimeFluxoDeTokens(self):
        
        fluxoDeTokens = open("fluxoDeTokens",'w')
        for token in self.fluxoDeTokens:
            fluxoDeTokens.write(token.toString()+", ")
        fluxoDeTokens.close()
    
    def imprimeTabelaDeToken(self):
        tabelaDeTokens = open("tabelaDeTokens",'w')
        t = PrettyTable(['Lexema', 'Linha', 'Coluna', 'Tipo do Token'])
        for token in self.fluxoDeTokens:
            t.add_row([str(token.getLexema()), str(token.getLinha()), str(token.getColuna()), str(token.getTipo())])
            #tabelaDeSimbolos.write("|" + str(indice) + "|" + str(self.tabelaDeSimbolos[indice] + "| \n"))
        tabelaDeTokens.write(str(t))
        tabelaDeTokens.close()
        
