import re

from leitorDeArquivos import LeitorDeArquivos
from tipoToken import TipoToken
from token import Token
from error import Error

class AnalisadorLexico:

    def __init__(self, nomeArquivo):
        self.arquivo = LeitorDeArquivos(nomeArquivo)
        self.arquivoLinhas = self.arquivo.linhasArquivo
        self.fluxoDeTokens = []
        self.tabelaDeSimbolos = {}
        self.operador = {"=": TipoToken.OPIgual , "==" : TipoToken.OPRecebe, ">": TipoToken.OPMaior, "++" : TipoToken.OPIncrementa, "&&" : TipoToken.OPAnd, "<=" : TipoToken.OPMenorIgual, "!" : TipoToken.OPNao, "-" : TipoToken.OPMenos, "--" : TipoToken.OPDecrementa, "+" : TipoToken.OPSoma, "+=" : TipoToken.OPSomaERecebe, "*": TipoToken.OpMultiplica }
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
    
    def ehIndiceValidoCol(self, indiceCol):
        if indiceCol < len(self.arquivoLinhas[indiceLinha]:
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
                # Testa se é um char Literal (v)
                
                #if not ehCharLiteral and caractere == '\'':
                if caractere == '\'':
                    if ehIndiceValidoCol(indiceColuna + 1):
                        c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                        if c1 == '\\':
                            c2 = self.arquivoLinhas[indiceLinha][indiceColuna + 2]
                            if  c2 == 'n' or c2 == 'r' or c2 == 't' or c2 == 'b' or c2 == 'f' or c2 == '\'' or c2 == '\"' or c2 == '\\' :
                                if ehIndiceValidoCol(indiceColuna + 3) and self.arquivoLinhas[indiceLinha][indiceColuna + 3] == '\'':
                                    self.geraToken(self.literal["char_literal"], caractere+c1+c2+c3)
                                    indiceColuna += 3
                                    continue
                                    
                                else: # c3 é diferente de aspas simples (')
                                    error = Error(indiceLinha, indiceColuna, "lexico", "não e char literal")
                                    
                            else: # c2 é diferente '\n' '\r' '\t' '\b' '\f' '\’' '\"' '\\'
                                error = Error(indiceLinha, indiceColuna, "lexico", "não e char literal")
                                
                        elif c1 != '\'' and c1 != '\\':
                            c2 = self.arquivoLinhas[indiceLinha][indiceColuna + 2]
                            if c2 == '\'':
                                self.geraToken(self.literal["char_literal"], caractere+c1+c2)
                                indiceColuna += 2
                                continue
                                
                            else: # c2 é diferente de aspas simples (')
                                error = Error(indiceLinha, indiceColuna, "lexico",  "não e char literal")
                                
                        else: # c1 for igual a aspas simples (') ou igual uma barra(\)
                            error = Error(indiceLinha, indiceColuna, "lexico",  "não e char literal")
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
                    print(lexema)
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
                    if caractere != 0:
                        c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1] 
                        if ehNumero(c1) and c1 != 0:
                            self.geraToken(self.literal["int_literal"], 0)
                            indiceColuna += 1
                            continue
                        else: # Caso proximo ao zero ainda seja um numero
                            error = Error(indiceLinha, indiceColuna, "lexico",  "não e um numero")
                    else:
                        while self.ehNumero(caractere):
                            indiceColuna += 1
                            caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                        lexema = self.arquivoLinhas[indiceLinha][iniLexema: (indiceColuna - 1)]
                        self.geraToken(self.literal["int_literal"], lexema)
                        continue
                #-------------------------------------------------------------



                #-------------------------------------------------------------
                # Testa se caracter é um operador (v)
                
                ehOperadorUni = False
                ehOperadorDup = False
                
                
                c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                
                if caractere == '=':
                    if c1 == '=':
                        ehOperadorDup = True
                elif caractere == '+':
                    if c1 == '+':
                        ehOperadorDup = True
                elif caractere == '&':
                    if c1 == '&':
                        ehOperadorDup = True
                elif caractere == '<':
                    if c1 == '=':
                        ehOperadorDup = True
                elif caractere == '-':
                    if c1 == '-':
                        ehOperadorDup = True
                elif caractere == '+':
                    if c1 == '=':
                        ehOperadorDup = True
                elif caractere in self.operador:
                    ehOperadorUni = True
                    ehOperadorDup = False
                
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
                    self.geraToken(self.operador[caractere], caractere)
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
        if tipoToken == "int_literal" or tipoToken == "char_literal" or tipoToken == "string_literal" or tipoToken == "variavel_literal":
            # Se o lexema não existir na tabela, então insere ele
            if lexema not in self.tabelaDeSimbolos:
                #O indice é vai ser dado pelo tamanho atual da tabela de simbolos
                #Insere o token na tabela de simbolos, cria o token e adiciona nno fluxo de tokens
                self.tabelaDeSimbolos[len(self.tabelaDeSimbolos)] = lexema
                token = Token(tipoToken,lexema, len(self.tabelaDeSimbolos))
                self.fluxoDeTokens.append(token)
                return
            else:
                #Se o token já existe, precisamos então ver com é o indice dele para inserir no fluxo de tokens
                index = [chave for (chave, valor) in self.tabelaDeSimbolos if valor == lexema] # <- é gambiarra, mas funciona.
                token = Token(tipoToken, lexema, chave)
                self.fluxoDeTokens.append(token)
                return
        else:
            # Se o lexema não for de um tipo que requer um tipo, então é só inserir este no fluxo de tokens
            token = Token(tipoToken, lexema)
            self.fluxoDeTokens.append(token)
            return
    
    def imprimeFluxoDeTokens(self):
        for token in self.fluxoDeTokens:
            print(token.toString())
