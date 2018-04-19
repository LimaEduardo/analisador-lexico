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
        self.operador = {"=": TipoToken.OPRecebe , "==" : TipoToken.OPIgual, ">": TipoToken.OPMaior, "++" : TipoToken.OPIncrementa, "&&" : TipoToken.OPAnd, "<=" : TipoToken.OPMenorIgual, "!" : TipoToken.OPNao, "-" : TipoToken.OPMenos, "--" : TipoToken.OPDecrementa, "+" : TipoToken.OPSoma, "+=" : TipoToken.OPSomaERecebe, "*": TipoToken.OpMultiplica }
        self.separador = {",": TipoToken.SepVirgula, "." : TipoToken.SepPonto, "[" : TipoToken.SepAbreColchete, "{" : TipoToken.SepAbreChave, "(" : TipoToken.SepAbreParentese, ")" : TipoToken.SepFechaParentese,"}" : TipoToken.SepFechaChave, "]" : TipoToken.SepFechaColchete, ";" : TipoToken.SepPontoEVirgula}
        self.reservada = {"abstract": TipoToken.PCAbstract, "boolean" : TipoToken.PCBoolean, "char" : TipoToken.PCChar, "class" : TipoToken.PCClass, "else" : TipoToken.PCElse ,"extends" : TipoToken.PCExtends ,"false" : TipoToken.PCFalse, "import" : TipoToken.PCImport, "if": TipoToken.PCIf ,"instanceof" : TipoToken.PCInstanceOf, "int" : TipoToken.PCInt, "new" : TipoToken.PCNew, "null" : TipoToken.PCNull, "package" : TipoToken.PCPackage, "private" : TipoToken.PCPrivate, "protected": TipoToken.PCProtected ,"public" : TipoToken.PCPublic, "return" : TipoToken.PCReturn, "static" : TipoToken.PCStatic, "super" : TipoToken.PCSuper, "this" : TipoToken.PCThis, "true" : TipoToken.PCTrue, "void" : TipoToken.PCVoid, "while" : TipoToken.PCWhile}
        self.literal = {"int_literal": TipoToken.Int, "char_literal": TipoToken.Char, "string_literal": TipoToken.String, "variavel_literal": TipoToken.Variavel}
        self.comentario = False
        self.string = False
    
    
    def ehCharIdentificador(self,c):
        if ((ord('a') <= ord(c)) and (ord(c) <= ord('z'))) or ((ord('A') <= ord(c)) and (ord(c) <= ord('Z'))) or c == '_' or c == '\$':
            return True
        else:
            return False
            
    def ehNumero(self,c):
        return c.isdigit()
    
    def ehOperador(self, c, c1):
        if c == '=':
            if c1 == '=':
                return True
        elif c == '+':
            if c1 == '+':
                return True
        elif c == '&':
            if c1 == '&':
                return True
        elif c == '<':
            if c1 == '=':
                return True
        elif c == '-':
            if c1 == '-':
                return True
        elif c == '+':
            if c1 == '=':
                return True
        elif c in self.operador:
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
                                        self.geraToken(self.literal["char_literal"], caractere+c1+c2+c3)
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
                                    self.geraToken(self.literal["char_literal"], caractere+c1+c2)
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
                    #while ((c != " ") and (not ehOperador(c)) and (c not in self.separador) and (c != "\t") and (c != "\n")):
                    while ((self.ehCharIdentificador(caractere)) or (self.ehNumero(caractere)) or (caractere == '_') or (caractere == '$')): 
                        indiceColuna += 1
                        caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                    
                    
                    lexema = self.arquivoLinhas[indiceLinha][iniLexema: (indiceColuna)]
                    if lexema not in self.reservada:  
                        self.geraToken(self.literal["variavel_literal"], lexema)
                        continue
                    else:
                        self.geraToken(self.reservada[lexema], lexema)
                        continue
                #-------------------------------------------------------------
                
                #-------------------------------------------------------------
                # Teste se é um numero (v)
                if self.ehNumero(caractere):
                    iniLexema = indiceColuna
                    if caractere == "0":
                        if self.ehIndiceValidoCol(indiceLinha, indiceColuna + 1):
                            c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                            
                            if((c1 == " ") or (self.ehOperador(caractere, c1)) or (c1 in self.separador) or (c1 == "\t") and (c1 == "\n")):
                                self.geraToken(self.literal["int_literal"], caractere)
                                indiceColuna += 1
                                continue
                            else: # Caso proximo ao zero  nao seja caracter valido
                                error = Error(indiceLinha, indiceColuna, "lexico",  "Numero Invalido")
                        else:
                            self.geraToken(self.literal["int_literal"], caractere)
                    else:
                        while self.ehNumero(caractere):
                            indiceColuna += 1
                            if self.ehIndiceValidoCol(indiceLinha, indiceColuna):
                                caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                            else:
                                caractere = None
                        lexema = self.arquivoLinhas[indiceLinha][iniLexema:indiceColuna]
                        self.geraToken(self.literal["int_literal"], lexema)
                        continue
                #-------------------------------------------------------------



                #-------------------------------------------------------------
                # Testa se caracter é um operador (v)
                
                ehOperadorUni = False
                ehOperadorDup = False
                
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
                    if ehOperadorUni:
                        self.geraToken(self.operador[caractere], caractere)
                        indiceColuna += 1
                        continue
                    elif ehOperadorDup:
                        self.geraToken(self.operador[caractere+c1], caractere+c1)
                        indiceColuna += 2
                        continue
                #-------------------------------------------------------------
                
                
                #-------------------------------------------------------------
                #testa se caractere é um separador (v)
                if caractere in self.separador:
                    self.geraToken(self.separador[caractere], caractere)
                    indiceColuna += 1
                    continue
                #else:
                 #   error = Error(indiceLinha, indiceColuna, "lexico",  "erro final")
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

    def geraToken(self, tipoToken, lexema):
        # Se é um desses tipos, deverá ser registrado na tabela de simbolos
        if tipoToken == self.literal["int_literal"] or tipoToken == self.literal["char_literal"] or tipoToken == self.literal["string_literal"] or tipoToken == self.literal["variavel_literal"]:
            #print (lexema, tipoToken)
            # Se o lexema não existir na tabela, então insere ele
            if lexema not in self.tabelaDeSimbolos.values():
                #O indice é vai ser dado pelo tamanho atual da tabela de simbolos
                #Insere o token na tabela de simbolos, cria o token e adiciona nno fluxo de tokens
                index = len(self.tabelaDeSimbolos)
                self.tabelaDeSimbolos[index] = lexema
                token = Token(tipoToken, lexema, index)
                self.fluxoDeTokens.append(token)
                return
            else:
                #Se o token já existe, precisamos então ver com é o indice dele para inserir no fluxo de tokens
                index = [chave for chave in self.tabelaDeSimbolos if self.tabelaDeSimbolos[chave] == lexema][0] # <- é gambiarra, mas funciona.
                token = Token(tipoToken, lexema, index)
                self.fluxoDeTokens.append(token)
                return
        else:
            # Se o lexema não for de um tipo que requer um tipo, então é só inserir este no fluxo de tokens
            token = Token(tipoToken, lexema)
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
