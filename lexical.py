import sys
import re
import shlex
import constants

#fileName = input("Enter filename: ")
file = open("a.cdsc", encoding="utf8")

readFile = file.read()
splitFile = readFile.split("\n")

print("Symbol Table Generated")

sys.stdout = open("Symbol Table.txt","w+")
print("Lexemes" .ljust(61) + "Tokens" )
print("-----------" .ljust(61) + "-----------" )
for line in splitFile:
    if re.search("^[#]#", line):
        print("{:60s} {:60s}".format(line, "singleLineComment"))
        continue
    if re.match("^[#][^\*\?]", line):
        print("{:60s} {:60s}".format(line, "invalidLexeme"))
        continue
    elif re.search("^[#]\?", line):
        print("{:60s} {:60s}".format(line, "singleLineQueryComment"))
        continue
    elif re.search("^[#\*][^*]*[*]+(?:[^/*][^*]*[*]+)[\*#]$", line):
        print("{:60s} {:60s}".format(line, "multipleLineComment"))
        continue
    elif (line.startswith("<???") and line.endswith("???>")):
        print("{:60s} {:60s}".format(line, "multipleLineQueryComment"))
        continue
    elif re.search(".?.:.", line):
        print("{:60s} {:60s}".format(line, "ternaryOp"))
        continue
    elif "int" in line:
        constants.dataTypePrint("int", line)
        continue
    elif "float" in line:
        constants.dataTypePrint("float", line)
        continue
    elif "double" in line:
        constants.dataTypePrint("double", line)
        continue
    else: 
        tokens = list(shlex.shlex(line, punctuation_chars="<>=+"))
        shlex.shlex.commenters = ''
    for token in tokens:
        if token in constants.arithmeticOp:
            print("{:60s} {:60s}".format(token, constants.arithmeticOp[token]))
        elif token in constants.assignmentOp:
            print("{:60s} {:60s}".format(token, constants.assignmentOp[token]))
        elif token in constants.delimitersAndBrackets:
            print("{:60s} {:60s}".format(token, constants.delimitersAndBrackets[token]))
        elif token in constants.relationalOp:
            print("{:60s} {:60s}".format(token, constants.relationalOp[token]))
        elif token in constants.logicalOp:
            print("{:60s} {:60s}".format(token, constants.logicalOp[token]))
        elif token in constants.unaryOp:
            print("{:60s} {:60s}".format(token, constants.unaryOp[token]))
        elif token in constants.groupingOP:
            print("{:60s} {:60s}".format(token, constants.groupingOP[token]))
        elif token in constants.noisewWord:
            print("{:60s} {:60s}".format(token, "noiseWord"))
        elif (token.startswith('"') and token.endswith('"')):
            if "\\n" in token:
                newlineCount = 0
                splitToken = token.split("\\n")
                for line2 in splitToken:
                    if "\\t" in line2:
                        tabCount = 0
                        anotherSplitToken = line2.split("\\t")
                        for line3 in anotherSplitToken:
                            if line3.startswith('"'):
                                print("{:60s} {:60s}".format(line3, "string"))
                                tabCount+=1
                            elif line3.endswith('"'):
                                print("{:60s} {:60s}".format(line3, "string"))
                                tabCount+=1
                            else:
                                print("{:60s} {:60s}".format(line3, "string"))
                                tabCount+=1
                            if tabCount == 1:
                                print("{:60s} {:60s}".format("\\t", "tab"))
                        newlineCount+=1
                    elif line2.startswith('"'):
                        print("{:60s} {:60s}".format(line2, "string"))
                        newlineCount+=1
                    elif line2.endswith('"'):
                        print("{:60s} {:60s}".format(line2, "string"))
                        newlineCount +=1
                    if newlineCount == 1:
                        print("{:60s} {:60s}".format("\\n", "newline"))
            elif "\\t" in token:
                tabCount = 0
                splitToken = token.split("\\t")
                for line2 in splitToken:
                    if line2.startswith('"'):
                        print("{:60s} {:60s}".format(line2, "string"))
                        tabCount+=1
                    elif line2.endswith('"'):
                        print("{:60s} {:60s}".format(line2, "string"))
                        tabCount+=1
                    if tabCount == 1:
                        print("\t {:60s} {:60s}".format("\\t", "tab"))
            else:
                print("{:60s} {:60s}".format(token, "string"))
        elif token in constants.reservedWord:
            print("{:60s} {:60s}".format(token, "reservedWord"))
        elif constants.identifier.search(token):
            print("{:60s} {:60s}".format(token, "identifier"))
        elif(re.findall(constants.number, token)):
            if("." in token):
                print("{:60s} {:60s}".format(token, "float_literal"))
            else:
                print("{:60s} {:60s}".format(token, "int_literal"))
        else:
            print("{:60s} {:60s}".format(token, "invalidLexeme"))        
file.close()