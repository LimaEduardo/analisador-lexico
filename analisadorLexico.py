from leitorDeArquivos import LeitorDeArquivos
from token import Token

class AnalisadorLexico:

    def __init__(self, nomeArquivo):
        arquivo = LeitorDeArquivos(nomeArquivo)
    
    def proximoToken(self):
        while char = arquivo.leProximoChar != None:
            c = str(char)
            if(c == " " or c == "\n"):
                continue
        return

    def identificaToken(self, token):

        if token == "=":
            return Token("OPRecebe", "=")
        elif token == "--":
            return Token("OPIgual", "==")
        elif token == ">":
            return Token("OPMaior", ">")
        elif token == "++":
            return Token("OPIncrementa", "++")
        elif token == "&&":
            return Token("OPAnd", "&&")
        elif token == "<=":
            return Token("OPMenorIgual", "<=")
        elif token == "!":
            return Token("OPNao", "!")
        elif token == "-":
            return Token("OPMenos", "-")
        elif token == "--":
            return Token("OPDecrementa", "--")
        elif token == "+":
            return Token("OPSoma", "+")
        elif token == "+=":
            return Token("OPSomaERecebe", "+=")
        elif token == "*":
            return Token("OPMultiplica", "*")
        elif token == ",":
            return Token("Virgula", ",")
        elif token == ".":
            return Token("Ponto", ".")
        elif token == "[":
            return Token("AbreColchete", "[")
        elif token == "{":
            return Token("AbreChave", "{")
        elif token == "(":
            return Token("AbreParentese", "(")
        elif token == ")":
            return Token("FechaParentese", ")")
        elif token == "}":
            return Token("FechaChave", "}")
        elif token == "]":
            return Token("FechaColchete", "]")
        elif token == ";":
            return Token("PontoEVirgula", ";")
        elif token == "abstract":
            return Token("PCAbstract", "abstract")
        elif token == "boolean":
            return Token("PCBoolean", "boolean")
        elif token == "char":
            return Token("PCChar", "char")
        elif token == "class":
            return Token("PCClass", "class")
        elif token == "else":
            return Token("PCElse", "else")
        elif token == "extends":
            return Token("PCExtends", "extends")
        elif token == "false":
            return Token("PCFalse", "false")
        elif token == "import":
            return Token("PCImport", "import")
        elif token == "if":
            return Token("PCIf", "if")
        elif token == "instanceof"
            return Token("PCInstanceOf", "instanceof")
        elif token == "int":
            return Token("PCInt", "int")
        elif token == "new":
            return Token("PCNew", "new")
        elif token == "null":
            return Token("PCNull", "null")
        elif token == "package":
            return Token("PCPackage", "package")
        elif token == "private":
            return Token("PCPrivate", "private")
        elif token == "protected":
            return Token("PCProtected", "protected")
        elif token == "public":
            return Token("PCPublic", "public")
        elif token == "return":
            return Token("PCReturn", "return")
        elif token == "static":
            return Token("PCStatic", "static")
        elif token == "super":
            return Token("PCSuper", "super")
        elif token == "this":
            return Token("PCThis", "this")
        elif token == "true":
            return Token("PCTrue", "true")
        elif token == "void":
            return Token("PCVoid", "void")
        elif token == "while":
            return Token("PCWhile", "while")