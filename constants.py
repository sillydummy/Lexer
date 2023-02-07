import re
import shlex

arithmeticOp = {
    '+': 'plusOp',
    '-': 'minusOp',
    '/': 'divideOp',
    '*': 'multiplyOp',
    '%': 'moduloOp',
    'times': 'timeswordOp',
    'divideBy': 'dividewordOp',
    'mod': 'modwordOp',
    'plus': 'pluswordOp',
    'minus': 'minuswordOp'
}
relationalOp = {
    '>': 'greaterthanOp',
    '<': 'lessthanOp',
    '>=': 'greaterthanorequalOp',
    '<=': 'lessthanorequalOp',
    'greaterThan': 'greaterthanwordOp',
    'lessThan': 'lessthanwordOp',
    'greaterThanOrEqual': 'greaterthanorequalwordOp',
    'lessThanOrEqual': 'lessthanorequalwordOp',
    '==': 'equalOp',
    '!=': 'notequalOp',
    '<>': 'notbracketsOp',
    'equalTo': 'isequalwordOp',
    'notEqualTo': 'notequalwordOp'
}
logicalOp = {
    '!': 'notOp',
    'NOT': 'notwordOp',
    '&&': 'andOp',
    'AND': 'andwordOp',
    '||': 'orOp',
    'OR': 'orwordOp'
}
assignmentOp = {
    '=': 'assignOp',
    'is': 'assignwordOp',
    '+=': 'plusequalOp',
    '-=': 'minusequalOp',
    '*=': 'timesequalOp',
    '/=': 'divideequalOp',
    '%=': 'moduloequalOp'
}
delimitersAndBrackets = {
    ';': 'semicolon',
    '.': 'dot', 
    ',': 'comma',
    '{': 'leftcurlybrace',
    '}': 'rightcurlybrace'
}
unaryOp = {
    '++': 'incrementOp',
    '--': 'decrementOp',       #aaysun
    '-': 'unarynegOp'
}
groupingOP = {
    '(': 'leftgroupingOp',
    ')': 'rightgroupingOp'
}
noisewWord = {
    'boolean': 'ean',
    'character': 'acter',
    'continue': 'inue',
    'integer': 'eger',
    'modulus': 'ulus'
}
whitespace = re.compile("\\d|\\n")
identifier = re.compile("^[a-zA-Z]+[a-zA-Z0-9]$")
number = re.compile("^[\d]+[\.]{0,1}[\d]*$")
reservedWord = ["int", "float", "char","string","double","bool","true", "false", "break", "cont", "for", "do", "while", "if", "else", "switch", "default", "input", "display", "int", "float", "double", "char", "string", "bool", "define", "void", "return", "var", "const"]
noise = ["ean", "acter", "inue", "eger", "ulus"]

def dataTypePrint(str, line):
    tokens = list(shlex.shlex(line, punctuation_chars="<>=+"))
    for token in tokens:
        if number.search(token): 
            print("{:60s} {:60s}".format(token, str + "_literal"))
        elif token in arithmeticOp:
            print("{:60s} {:60s}".format(token, arithmeticOp[token]))
        elif token in assignmentOp:
            print("{:60s} {:60s}".format(token, assignmentOp[token]))
        elif token in delimitersAndBrackets:
            print("{:60s} {:60s}".format(token, delimitersAndBrackets[token]))
        elif token in relationalOp:
            print("{:60s} {:60s}".format(token, relationalOp[token]))
        elif token in logicalOp:
            print("{:60s} {:60s}".format(token, logicalOp[token]))
        elif token in unaryOp:
            print("{:60s} {:60s}".format(token, unaryOp[token]))
        elif token in groupingOP:
            print("{:60s} {:60s}".format(token, groupingOP[token]))
        elif token in noisewWord:
            print("{:60s} {:60s}}".format(token, "noiseWord"))
        elif (token.startswith('"') and token.endswith('"')):
            print("{:60s} {:60s}".format(token, "string"))
        elif token in reservedWord:
            print("{:60s} {:60s}".format(token, "reservedWord"))
        elif identifier.search(token):
            print("{:60s} {:60s}".format(token, "identifier"))
        else:
            print("{:60s} {:60s}".format(token, "invalidLexeme"))