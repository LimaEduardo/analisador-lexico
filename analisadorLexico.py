import re

from leitorDeArquivos import LeitorDeArquivos
from tipoToken import TipoToken
from token import Token

class AnalisadorLexico:

    def __init__(self, nomeArquivo):
        self.arquivo = LeitorDeArquivos(nomeArquivo)
        self.arquivoLinhas = arquivo.linhasArquivo
        self.fluxoDeTokens = []
        self.tabelaDeSimbolos = {}
        self.operador = {"=": TipoToken.OPIgual , "==" : TipoToken.OPRecebe, ">": TipoToken.OPMaior, "++" : TipoToken.OPIncrementa, "&&" : TipoToken.OPAnd, "<=" : TipoToken.OPMenorIgual, "!" : TipoToken.OPNao, "-" : TipoToken.OPMenos, "--" : TipoToken.OPDecrementa, "+" : TipoToken.OPSoma, "+=" : TipoToken.OPSomaERecebe, "*": TipoToken.OpMultiplica }
        self.separador = {",": TipoToken.SepVirgula, "." : TipoToken.SepPonto, "[" : TipoToken.SepAbreColchete, "{" : TipoToken.SepAbreChave, "(" : TipoToken.SepAbreParentese, ")" : TipoToken.SepFechaParentese,"}" : TipoToken.SepFechaChave, "]" : TipoToken.SepFechaColchete, ";" : TipoToken.SepPontoEVirgula}
        self.reservada = {"abstract": TipoToken.PCAbstract, "boolean" : TipoToken.PCBoolean, "char" : TipoToken.PCChar, "class" : TipoToken.PCClass, "else" : TipoToken.PCElse ,"extends" : TipoToken.PCExtends ,"false" : TipoToken.PCFalse, "import" : TipoToken.PCImport, "if": TipoToken.PCIf ,"instanceof" : TipoToken.PCInstanceOf, "int" : TipoToken.PCInt, "new" : TipoToken.PCNew, "null" : TipoToken.PCNull, "package" : TipoToken.PCPackage, "private" : TipoToken.PCPrivate, "protected": TipoToken.PCProtected ,"public" : TipoToken.PCPublic, "return" : TipoToken.PCReturn, "static" : TipoToken.PCStatic, "super" : TipoToken.PCSuper, "this" : TipoToken.PCThis, "true" : TipoToken.PCTrue, "void" : TipoToken.PCVoid, "while" : TipoToken.PCWhile}
        self.comentario = False
        self.string = False
    
    
    def ehCharIdentificador(self,c):
        if ((ord('a') <= ord(c)) and (ord(c) <= ord('z')) or
           ((ord('A') <= ord(c)) and (ord(c) <= ord('Z')) or
           c == '_' or c == '$':
            return True
        else
            return False
            
    def ehNumero(self,c):
        return c.isdigit():
    
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
        else
            return False
    
    def analisa(self):
        ehIdentificador = False
        ehIntLiteral = False
        ehStringLiteral = False
        ehSeparador = False
        ehOperadorUni = False
        ehOperadorDup = False
        ehPalavraChave = False
        
        iniLexema = 0
        indiceLinha = 0
        while (indiceLinha < len(self.arquivoLinhas)):
            indiceColuna = 0
            while (indiceColuna < len(self.arquivoLinhas[indiceLinha])):
                indiceColuna = 0
                caractere = self.arquivoLinhas[indiceLinha][indiceColuna]
                
                #-------------------------------------------------------------
                # Testa se é um char Literal
                if not ehCharLiteral and caractere == '\'':
                    c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]       
                    if c1 == '\\':
                        c2 = self.arquivoLinhas[indiceLinha][indiceColuna + 2]
                        if  c2 == 't' or c2 == 'b' or c2 == 'f' or c2 == '\'' or c2 == '\"' or c2 == '\\' :
                            if self.arquivoLinhas[indiceLinha][indiceColuna + 3] == '\'':
                                self.resolve(token("char_literal", caractere+c1+c2+c3)
                                indiceColuna += 3
                                continue
                    elif c1 != '\'' and c1 != '/':
                        c2 = self.arquivoLinhas[indiceLinha][indiceColuna + 2]
                        if c2 == '\'':
                            self.resolve(token("char_literal", caractere+c1+c2)
                            indiceColuna += 2
                            continue
                #-------------------------------------------------------------
                
                
                
                #-------------------------------------------------------------
                # Teste se achou um identificador
                if ehCharIdentificador(caractere):
                    iniLexema = indiceColuna
                    while ((c != " ") and (not ehOperador(c)) and (c not in self.separador) and (c != "\t")):
                        indiceColuna += 1
                    lexema = self.arquivoLinhas[indiceLinha][iniLexema: indiceColuna]
                    if lexema not in self.reservada
                        self.resolve(token("Variavel", lexema))  
                    else
                        self.resolve(self.operador[lexema])
                #-------------------------------------------------------------
                
                #-------------------------------------------------------------
                #Teste se é um numero
                if ehNumero(caractere):
                    iniLexema = indiceColuna
                    while ((c != " ") and (not ehOperador(c)) and (c not in self.separador) and (c != "\t")):
                        indiceColuna += 1
                    lexema = self.arquivoLinhas[indiceLinha][iniLexema: indiceColuna]
                    self.resolve(token("Int", lexema)
                #-------------------------------------------------------------



                #-------------------------------------------------------------
                #Testa se caracter é um operador
                c1 = self.arquivoLinhas[indiceLinha][indiceColuna + 1]
                if caractere == '=':
                    if  == '=':
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
                #Criando os tokens de um operador
                if ehOperadorUni:
                    self.resolve(self.operador[caracter])
                    indiceColuna += 1
                    continue
                elif ehOperadorDup:
                    self.resolve(self.operador[caracter+c1])
                    indiceColuna += 2
                    continue
                #-------------------------------------------------------------
                
                
                #-------------------------------------------------------------
                #testa se caractere é um separador
                if caractere in self.separador:
                    self.resolve(self.operador[caracter])
                    indiceColuna += 1
                    continue
                #-------------------------------------------------------------
                
            indiceLinha += 1
                
        while c != None:

            if self.comentario and c == "\n":
                self.comentario = False
                self.lexema = []

            if self.comentario:
                c = self.arquivo.leProximoChar()
                continue

            if ''.join(self.lexema) == "//":
                self.comentario = True

            if (not self.comentario) and (c in self.separador or c in self.operador or c == " " or c == "\n"):
                cadeia = ''.join(self.lexema)
                if cadeia is not '':
                    print(''.join(self.lexema))
                    self.resolveToken(self.identificaToken(cadeia))
                self.lexema = []
            else:
                self.lexema.append(c)
            c = self.arquivo.leProximoChar()
    
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

    def resolveToken(self, tipoToken, lexema):
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
