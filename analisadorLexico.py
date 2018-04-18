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
    
    # def proximoToken(self):
    #     while char = arquivo.leProximoChar != None:
    #         c = str(char)
    #         if(c == " " or c == "\n"):
    #             continue
    #     return
    
    def analisa(self):
        c = self.arquivo.leProximoChar()
        while c != None:    
            if self.separador(c) or self.operador(c) or c == " ":
                cadeia = ''.join(self.buffer)
                if cadeia is not '':
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
        tipo = token.getTipo()
        if tipo == "int_literal" or tipo == "char_literal" or tipo == "string_literal":
            if token.getLexema() not in self.tabelaDeSimbolos:
                self.tabelaDeSimbolos[len(self.tabelaDeSimbolos)] = lexema
        self.fluxoDeTokens.append(token)
        print(self.fluxoDeTokens)
    
    def imprimeFluxoDeTokens(self):
        print(self.fluxoDeTokens)


    def identificaToken(self, cadeiaDeCaracteres):
        # tipo = str(TipoToken[cadeiaDeCaracteres].value[1])
        # if tipo == "operador":
        print(self.buffer)
        if cadeiaDeCaracteres == "=":
            return Token("OPRecebe", "=")
        elif cadeiaDeCaracteres == "--":
            return Token("OPIgual", "==")
        elif cadeiaDeCaracteres == ">":
            return Token("OPMaior", ">")
        elif cadeiaDeCaracteres == "++string_literal":
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

        # elif tipo == "separador":
        elif cadeiaDeCaracteres == ",":
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
        
        # elif tipo == "reservada":
        elif cadeiaDeCaracteres == "abstract":
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
            if re.match(padraoNumero, cadeiaDeCaracteres):
                return Token("int_literal", cadeiaDeCaracteres, 0)
            elif re.match(padraoChar, cadeiaDeCaracteres):
                return Token("char_literal", cadeiaDeCaracteres, 0)
            elif re.match(padraoString, cadeiaDeCaracteres):
                return Token("string_literal", cadeiaDeCaracteres, 0)