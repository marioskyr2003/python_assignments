import math

def asciitoBinary(a): #Function that converts ascii characters to binary (coverted in string for the purpose of the seq. caclulation)
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(str(bin(i)[2:]))
  return m

def BiggestSeqOf(num,lines): #function that calculates the biggest sequence of a number(num) in a list of numbers
    num=str(num)
    cmax=0
    f = 'false'
    for k in range (len(lines)):
        c=0
        for i in range (len(lines[k])):
            if lines[k][i] == num:
                c += 1
                f = 'true'
                if (i == len(lines[k])-1):
                    if (cmax < c):
                        cmax = c
            else:
                if (f == 'true'):
                    if (cmax < c):
                        cmax = c
                    c=0
                f = 'false'
    return cmax
    
try:
    file=open("two_cities_ascii.txt")
except FileNotFoundError:
    print("Error! File not found")
else:
    print('Opening file...')
    lines=file.read()
    print('Converting ASCII file to binary...')
    lines=asciitoBinary(lines)
    print('Calculating...')
    max0=BiggestSeqOf(0,lines)
    max1=BiggestSeqOf(1,lines)
                
    file.close()
    print('\n-----------------------Done-----------------------\nBiggest Sequence of 0s:',max0,'\nBiggest Sequence of 1s:',max1)