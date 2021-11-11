import math
import copy
import random

def printQuads():
    print(quads)
    
def QuadgramSetup():
    global quads
    f = open("english_quadgrams.txt","r")
    quads = {}
    total = 0
    for line in f:
        line = line.rstrip()
        quad = line.split(" ")[0]
        freq = int(line.split(" ")[1])
        total += freq
        quads[quad] = freq
        
    f.close()
    for quadK in quads.keys():
        #print(quads[quadK])
        ans = quads[quadK]/float(total)
        #print(ans)
        quads[quadK] = math.log(ans)

    
    
def GetLikelihood(text):
    global quads
    total = 0
    for j,letter2 in enumerate(text):
        #print(str(j) + " " + str(len(text)) )
        if j + 3 < len(text):
            quad =  letter2 + text[j+1] + text[j+2] + text[j+3] 
        if quad in quads:
            total += quads[quad]
        else:
            total -= 10 # math.log(0.0001)
    return float(total)

def ioc(text):
    freqs = []
    for i in range(26):
        freqs.append(0)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i,letter in enumerate(alphabet):
        freqs[i] = text.count(letter)
        total = 0
    for i,freq in enumerate(freqs):
        total += freq * freq-1
    answer = (len(text) * (len(text)-1))
    total = total/float(answer) 
    return total

def ChiSquared(text):
    probabilities = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
    counts = []
    length = len(text)
    for prob in probabilities:
        counts.append(length * prob)

    countsInText = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #print(text)
    for char in text:
        countsInText[alphabet.index(char)] += 1

    total = 0
    for i,count in enumerate(countsInText):
        tophalf = (count - counts[i]) ** 2
        bottomhalf = counts[i]
        total += (tophalf/float(bottomhalf))
    return total