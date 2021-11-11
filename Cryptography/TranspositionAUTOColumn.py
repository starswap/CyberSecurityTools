#Write by row; read by columns method

#Import necessary packages including my own
import copy
import math
import collections
import itertools
from statistics import QuadgramSetup, GetLikelihood

#Get cipher text and remove special characters
text = raw_input("Enter text:").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = text.replace(" ","")
text = text.replace(".","")
text = text.replace(",","")
text = text.replace(":","")
text = text.replace("'","")
text = text.replace(";","")

#Set up the Quadgram score fitness metric which will be used to determine the best solution 
QuadgramSetup()

#Save to use when padding
originalText = text

#For each possible key length
for count in range(1,10):
    
    #Top 5 plain texts for each key length
    bestPlains = ["","","","",""]
    bestLikelihoods = [-1000000,-1000000,-1000000,-1000000,-1000000]
    bestKeys = ["","","","",""]

    #Padding
    if len(originalText) % count != 0:
        text = originalText + (((((len(originalText) // count) + 1) * count) - len(originalText)) * ".")
    else:
        text = originalText

    #We will brute force all keys
    keys = []
    print(alphabet[:count]) # Shows the user the current key length being tried
    
    #Get all possible keys
    for item in itertools.permutations(alphabet[:count], count):
        string = ''.join(item)
        keys.append(string)

    #For all possible keys
    for keyNumber,keyword in enumerate(keys):
        
        alphKey = ''.join(sorted(keyword)) 
        rows = int(len(text)/len(keyword))
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
        for i,num in enumerate(bestLikelihoods):
            if Final == bestPlains[i]:
                break
            if like > float(num):
                bestPlains[i] = Final
                bestLikelihoods[i] = like
                bestKeys[i] = keyword
                break
        if keyNumber % 1000 == 0:
            print(keyNumber)
            
    print(bestPlains[0])
