import constants
import re
import shlex

file = open("Symbol Table.txt", encoding="utf8")

readFile = file.read()
splitFile = shlex.split(readFile)

ctr = 0

def parseMain(token):
    if token in constants.reservedWord:
        variableParse(token)
def variableParse(token):
    print(token)

for line in splitFile:
    if ctr < 4:
        ctr+=1
        continue
    for i in range(2, ctr):
        if (ctr % i) == 0:
            parseMain(line)
            ctr+=1
            break
        else:
            ctr+=1
            break

        

    
