import re

from leitorDeArquivos import LeitorDeArquivos
from tipoToken import TipoToken
from token import Token

class AnalisadorLexico:

    def __init__(self, nomeArquivo):
        self.arquivo = LeitorDeArquivos(nomeArquivo)
        self.buffer = []
        self.fluxoDeTokens = []
        self.tabelaDeSimbolos = {}
        self.operador = {"=", "==", ">", "++", "&&", "<=", "!", "-", "--", "+", "+=", "*" }
        self.separador = {",", ".", "[", "{", "(", ")","}", "]", ";"}
        self.reservada = {"abstract", "boolean", "char", "class", "else" ,"extends" ,"false", "import", "if" ,"instanceof", "int", "new", "null", "package", "private", "protected" ,"public", "return", "static", "super", "this", "true", "void", "while"}
        self.comentario = False
    
    # def proximoToken(self):
    #     while char = arquivo.leProximoChar != None:
    #         c = str(char)
    #         if(c == " " or c == "\n"):
    #             continue
    #     return
    
    def analisa(self):
        c = self.arquivo.leProximoChar()
        while c != None:
            if self.comentario:
                continue

            if self.comentario and c == "\n":
                self.comentario = False
                self.buffer = []

            if ''.join(self.buffer) == "//":
                self.comentario = True

            if (c in self.separador or c in self.operador or c == " " or c == "\n") and (not self.comentario):
                cadeia = ''.join(self.buffer)
                if cadeia is not '':
                    print(''.join(self.buffer))
                    self.resolveToken(self.identificaToken(cadeia))
                self.buffer = []
            else:
                self.buffer.append(c)
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
        print(token)
        tipo = token.getTipo()
        print(tipo)
        if tipo == "int_literal" or tipo == "char_literal" or tipo == "string_literal":
            if token.getLexema() not in self.tabelaDeSimbolos:
                self.tabelaDeSimbolos[len(self.tabelaDeSimbolos)] = token.getLexema()
        self.fluxoDeTokens.append(token)
        print(self.fluxoDeTokens)
    
    def imprimeFluxoDeTokens(self):
        print(self.fluxoDeTokens)


    def identificaToken(self, cadeiaDeCaracteres):
        # tipo = str(TipoToken[cadeiaDeCaracteres].value[1])
        print(self.buffer)
        if cadeiaDeCaracteres in self.operador:
            if cadeiaDeCaracteres == "=":
                return Token("OPRecebe", "=")
            elif cadeiaDeCaracteres == "==":
                return Token("OPIgual", "==")
            elif cadeiaDeCaracteres == ">":
                return Token("OPMaior", ">")
            elif cadeiaDeCaracteres == "++":
                return Token("OPIncrementa", "++")
            elif cadeiaDeCaracteres == "&&":
                return Token("OPAnd", "&&")
            elif cadeiaDeCaracteres == "<=":
                return Token("OPMenorIgual", "<=")
            elif cadeiaDeCaracteres == "!":
                return Token("OPNao", "!")
            elif cadeiaDeCaracteres == "-":
                return Token("OPMenos", "-")
            elif cadeiaDeCaracteres == "--":
                return Token("OPDecrementa", "--")
            elif cadeiaDeCaracteres == "+":
                return Token("OPSoma", "+")
            elif cadeiaDeCaracteres == "+=":
                return Token("OPSomaERecebe", "+=")
            elif cadeiaDeCaracteres == "*":
                return Token("OPMultiplica", "*")

        elif cadeiaDeCaracteres in self.separador:
            if cadeiaDeCaracteres == ",":
                return Token("Virgula", ",")
            elif cadeiaDeCaracteres == ".":
                return Token("Ponto", ".")
            elif cadeiaDeCaracteres == "[":
                return Token("AbreColchete", "[")
            elif cadeiaDeCaracteres == "{":
                return Token("AbreChave", "{")
            elif cadeiaDeCaracteres == "(":
                return Token("AbreParentese", "(")
            elif cadeiaDeCaracteres == ")":
                return Token("FechaParentese", ")")
            elif cadeiaDeCaracteres == "}":
                return Token("FechaChave", "}")
            elif cadeiaDeCaracteres == "]":
                return Token("FechaColchete", "]")
            elif cadeiaDeCaracteres == ";":
                return Token("PontoEVirgula", ";")
        
        elif cadeiaDeCaracteres in self.reservada:
            if cadeiaDeCaracteres == "abstract":
                return Token("PCAbstract", "abstract")
            elif cadeiaDeCaracteres == "boolean":
                return Token("PCBoolean", "boolean")
            elif cadeiaDeCaracteres == "char":
                return Token("PCChar", "char")
            elif cadeiaDeCaracteres == "class":
                return Token("PCClass", "class")
            elif cadeiaDeCaracteres == "else":
                return Token("PCElse", "else")
            elif cadeiaDeCaracteres == "extends":
                return Token("PCExtends", "extends")
            elif cadeiaDeCaracteres == "false":
                return Token("PCFalse", "false")
            elif cadeiaDeCaracteres == "import":
                return Token("PCImport", "import")
            elif cadeiaDeCaracteres == "if":
                return Token("PCIf", "if")
            elif cadeiaDeCaracteres == "instanceof":
                return Token("PCInstanceOf", "instanceof")
            elif cadeiaDeCaracteres == "int":
                return Token("PCInt", "int")
            elif cadeiaDeCaracteres == "new":
                return Token("PCNew", "new")
            elif cadeiaDeCaracteres == "null":
                return Token("PCNull", "null")
            elif cadeiaDeCaracteres == "package":
                return Token("PCPackage", "package")
            elif cadeiaDeCaracteres == "private":
                return Token("PCPrivate", "private")
            elif cadeiaDeCaracteres == "protected":
                return Token("PCProtected", "protected")
            elif cadeiaDeCaracteres == "public":
                return Token("PCPublic", "public")
            elif cadeiaDeCaracteres == "return":
                return Token("PCReturn", "return")
            elif cadeiaDeCaracteres == "static":
                return Token("PCStatic", "static")
            elif cadeiaDeCaracteres == "super":
                return Token("PCSuper", "super")
            elif cadeiaDeCaracteres == "this":
                return Token("PCThis", "this")
            elif cadeiaDeCaracteres == "true":
                return Token("PCTrue", "true")
            elif cadeiaDeCaracteres == "void":
                return Token("PCVoid", "void")
            elif cadeiaDeCaracteres == "while":
                return Token("PCWhile", "while")
        else:
            # [1-9]?[0-9]* numero
            padraoNumero = re.compile("^[1-9]?[0-9]*$")
            padraoChar = re.compile("^'\w'$")
            padraoString = re.compile("^'(\w)*'$")
            padraoVariavel = re.compile("^(\w)*$")
            if re.match(padraoNumero, cadeiaDeCaracteres):
                return Token("int_literal", cadeiaDeCaracteres, 0)
            elif re.match(padraoChar, cadeiaDeCaracteres):
                return Token("char_literal", cadeiaDeCaracteres, 0)
            elif re.match(padraoString, cadeiaDeCaracteres):
                return Token("string_literal", cadeiaDeCaracteres, 0)
            elif re.match(padraoVariavel, cadeiaDeCaracteres):
                return Token("variavel_literal", cadeiaDeCaracteres, 0)