#! python3

import re
import os
import docx

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for st in table[i]:
            if len(st) > colWidths[i]:
                colWidths[i] = len(st)
    for i in range(len(table[0])):
        line = ""
        for j in range(len(table)):
            line += table[j][i].rjust(colWidths[j])+" "
        print(line)


def strong_pass(pas):
    nrreg = re.compile(r'.{8,}')
    letreg = re.compile(r'[a-z][A-Z]|[A-Z][a-z]')
    numreg = re.compile(r'[0-9]')
    if nrreg.search(pas) is None or letreg.search(pas) is None or numreg.search(pas) is None:
        print('Weak password')
    else:
        print('Strong password')


def new_strip(text, ch=""):
    reg = "\\s"
    if ch != "":
        reg += "|"+ch
    print(reg)
    space = re.compile(reg)
    return space.sub('', text)


# printTable(tableData)
# strong_pass('Alabala1')
# print(new_strip('   asdasd  ', "a"))
print(os.getcwd())
