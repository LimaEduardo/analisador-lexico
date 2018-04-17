from enum import Enum

class TipoToken(Enum): 
    PCAbstract = ("abstract", "reservada")
    PCBoolean = ("boolean", "reservada")
    PCChar = ("char", "reservada")
    PCClass = ("class","reservada")
    PCElse = ("else","reservada")
    PCExtends = ("extends","reservada")
    PCFalse = ("false","reservada")
    PCImport = ("import","reservada")
    PCIf = ("if","reservada")
    PCInstanceOf = ("instanceof","reservada")
    PCInt = ("int", "reservada")
    PCNew = ("new", "reservada")
    PCNull = ("null", "reservada")
    PCPackage = ("package", "reservada")
    PCPrivate = ("private", "reservada")
    PCProtected = ("protected", "reservada")
    PCPublic = ("public", "reservada")
    PCReturn = ("return", "reservada")
    PCStatic = ("static", "reservada")
    PCSuper = ("super", "reservada")
    PCThis = ("this", "reservada")
    PCTrue = ("true", "reservada")
    PCVoid = ("void", "reservada")
    PCWhile = ("while", "reservada")

    OPRecebe = ("=", "operador")
    OPIgual = ("==", "operador")
    OPMaior = (">", "operador")
    OPIncrementa = ("++", "operador")
    OPAnd = ("&&", "operador")
    OPMenorIgual = ("<=", "operador")
    OPNao = ("!", "operador")
    OPMenos  = ("-", "operador")
    OPDecrementa = ("--", "operador")
    OPSoma = ("+", "operador")
    OPSomaERecebe = ("+=", "operador")
    OpMultiplica = ("*", "operador")
    
    Virgula = (",", "separador")
    Ponto = (".", "separador")
    AbreColchete = ("[","separador")
    AbreChave = ("{","separador")
    AbreParentese = ("(","separador")
    FechaParentese = (")","separador")
    FechaChave = ("}","separador")
    FechaColchete = ("]","separador")
    PontoEVirgula = (";","separador")