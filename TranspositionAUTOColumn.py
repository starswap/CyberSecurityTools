#It tends to be the later transpositions that use this method. Use other program - transposition AUTO Row if it's read off by row
#This program will automatically run through all possible keys up to length ten, using the read off by columns method. If read off by row, you can use the autopad program and then the row program. This is the method employed by Practical and by default by dcode.fr.

import copy
import math
import collections
from statistics import QuadgramSetup, GetLikelihood
text = raw_input("Enter text:").upper()
#keyword = raw_input("enter keyword").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = text.replace(" ","")
text = text.replace(".","")
text = text.replace(",","")
text = text.replace(":","")
text = text.replace("'","")
text = text.replace(";","")

QuadgramSetup()

import itertools

count = 9 # keyLength
print(alphabet[:count])


bestPlains = ["","","","",""]
bestLikelihoods = [-1000000,-1000000,-1000000,-1000000,-1000000]
bestKeys = ["","","","",""]

originalText = text
for count in range(1,10):
    
    if len(originalText) % count != 0:
        text = originalText + (((((len(originalText) // count) + 1) * count) - len(originalText)) * ".")
    else:
        text = originalText
    print(count)
    print(text)


    keys= []
    print(alphabet[:count])
    for item in itertools.permutations(alphabet[:count], count):
        string = ''.join(item)
        keys.append(string)

    for keyNumber,keyword in enumerate(keys):
        alphKey = ''.join(sorted(keyword))
        rows = int(len(text)/len(keyword))
    #print(table)
    #Decrypt = {}
        chars = []
        for i in range (len(alphKey)):
            chars.append(text[i*rows:(i+1)*rows])
            decrypt = []
        for thing in chars:
            decrypt.append([])
        for i,char in enumerate(alphKey):
            decrypt[keyword.index(char)] = chars[i]
            keyword = keyword[:keyword.index(char)] + " " + keyword[keyword.index(char) + 1:]

    
        Final = ""
        for i in range(len(decrypt[0])):
            for col in decrypt:
                Final += col[i]
        like = float(GetLikelihood(Final))
        #print(like)
        for i,num in enumerate(bestLikelihoods):
        #   print(num)
          #  print(i)
            if Final == bestPlains[i]:
                break
            if like > float(num):
                bestPlains[i] = Final
                bestLikelihoods[i] = like
                bestKeys[i] = keyword
                break
        if keyNumber % 1000 == 0:
          # print(bestPlains)
            print(keyNumber)
    print(bestPlains[0])
