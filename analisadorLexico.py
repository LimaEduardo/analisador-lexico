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

    
    def resolveToken(self, token):
        tipo = token.getTipo()
        if tipo == "int_literal" or tipo == "char_literal" or tipo == "string_literal":
            if token.getLexema() not in self.tabelaDeSimbolos:
                self.tabelaDeSimbolos[len(self.tabelaDeSimbolos)] = token.getLexema()
        self.fluxoDeTokens.append(token)
        self.imprimeFluxoDeTokens()


    # def identificaToken(self, cadeiaDeCaracteres):
    #     # tipo = str(TipoToken[cadeiaDeCaracteres].value[1])
    #     print(self.lexema)
    #     if cadeiaDeCaracteres in self.operador:
    #         if cadeiaDeCaracteres == "=":
    #             return Token("OPRecebe", "=")
    #         elif cadeiaDeCaracteres == "==":
    #             return Token("OPIgual", "==")
    #         elif cadeiaDeCaracteres == ">":
    #             return Token("OPMaior", ">")
    #         elif cadeiaDeCaracteres == "++":
    #             return Token("OPIncrementa", "++")
    #         elif cadeiaDeCaracteres == "&&":
    #             return Token("OPAnd", "&&")
    #         elif cadeiaDeCaracteres == "<=":
    #             return Token("OPMenorIgual", "<=")
    #         elif cadeiaDeCaracteres == "!":
    #             return Token("OPNao", "!")
    #         elif cadeiaDeCaracteres == "-":
    #             return Token("OPMenos", "-")
    #         elif cadeiaDeCaracteres == "--":
    #             return Token("OPDecrementa", "--")
    #         elif cadeiaDeCaracteres == "+":
    #             return Token("OPSoma", "+")
    #         elif cadeiaDeCaracteres == "+=":
    #             return Token("OPSomaERecebe", "+=")
    #         elif cadeiaDeCaracteres == "*":
    #             return Token("OPMultiplica", "*")

    #     elif cadeiaDeCaracteres in self.separador:
    #         if cadeiaDeCaracteres == ",":
    #             return Token("Virgula", ",")
    #         elif cadeiaDeCaracteres == ".":
    #             return Token("Ponto", ".")
    #         elif cadeiaDeCaracteres == "[":
    #             return Token("AbreColchete", "[")
    #         elif cadeiaDeCaracteres == "{":
    #             return Token("AbreChave", "{")
    #         elif cadeiaDeCaracteres == "(":
    #             return Token("AbreParentese", "(")
    #         elif cadeiaDeCaracteres == ")":
    #             return Token("FechaParentese", ")")
    #         elif cadeiaDeCaracteres == "}":
    #             return Token("FechaChave", "}")
    #         elif cadeiaDeCaracteres == "]":
    #             return Token("FechaColchete", "]")
    #         elif cadeiaDeCaracteres == ";":
    #             return Token("PontoEVirgula", ";")
        
    #     elif cadeiaDeCaracteres in self.reservada:
    #         if cadeiaDeCaracteres == "abstract":
    #             return Token("PCAbstract", "abstract")
    #         elif cadeiaDeCaracteres == "boolean":
    #             return Token("PCBoolean", "boolean")
    #         elif cadeiaDeCaracteres == "char":
    #             return Token("PCChar", "char")
    #         elif cadeiaDeCaracteres == "class":
    #             return Token("PCClass", "class")
    #         elif cadeiaDeCaracteres == "else":
    #             return Token("PCElse", "else")
    #         elif cadeiaDeCaracteres == "extends":
    #             return Token("PCExtends", "extends")
    #         elif cadeiaDeCaracteres == "false":
    #             return Token("PCFalse", "false")
    #         elif cadeiaDeCaracteres == "import":
    #             return Token("PCImport", "import")
    #         elif cadeiaDeCaracteres == "if":
    #             return Token("PCIf", "if")
    #         elif cadeiaDeCaracteres == "instanceof":
    #             return Token("PCInstanceOf", "instanceof")
    #         elif cadeiaDeCaracteres == "int":
    #             return Token("PCInt", "int")
    #         elif cadeiaDeCaracteres == "new":
    #             return Token("PCNew", "new")
    #         elif cadeiaDeCaracteres == "null":
    #             return Token("PCNull", "null")
    #         elif cadeiaDeCaracteres == "package":
    #             return Token("PCPackage", "package")
    #         elif cadeiaDeCaracteres == "private":
    #             return Token("PCPrivate", "private")
    #         elif cadeiaDeCaracteres == "protected":
    #             return Token("PCProtected", "protected")
    #         elif cadeiaDeCaracteres == "public":
    #             return Token("PCPublic", "public")
    #         elif cadeiaDeCaracteres == "return":
    #             return Token("PCReturn", "return")
    #         elif cadeiaDeCaracteres == "static":
    #             return Token("PCStatic", "static")
    #         elif cadeiaDeCaracteres == "super":
    #             return Token("PCSuper", "super")
    #         elif cadeiaDeCaracteres == "this":
    #             return Token("PCThis", "this")
    #         elif cadeiaDeCaracteres == "true":
    #             return Token("PCTrue", "true")
    #         elif cadeiaDeCaracteres == "void":
    #             return Token("PCVoid", "void")
    #         elif cadeiaDeCaracteres == "while":
    #             return Token("PCWhile", "while")
    #     else:
    #         # [1-9]?[0-9]* numero
    #         padraoNumero = re.compile("^[1-9]?[0-9]*$")
    #         padraoChar = re.compile("^'\w'$")
    #         padraoString = re.compile("^\"(\w)*\"$")
    #         padraoVariavel = re.compile("^(\w)*$")
    #         if re.match(padraoNumero, cadeiaDeCaracteres):
    #             return Token("int_literal", cadeiaDeCaracteres, 0)
    #         elif re.match(padraoChar, cadeiaDeCaracteres):
    #             return Token("char_literal", cadeiaDeCaracteres, 0)
    #         elif re.match(padraoString, cadeiaDeCaracteres):
    #             return Token("string_literal", cadeiaDeCaracteres, 0)
    #         elif re.match(padraoVariavel, cadeiaDeCaracteres):
    #             return Token("variavel_literal", cadeiaDeCaracteres, 0)
