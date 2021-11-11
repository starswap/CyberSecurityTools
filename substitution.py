import random
import copy
import math
from statistics import GetLikelihood, QuadgramSetup
from utilities import InputText
text = InputText()
result = (-9.82289*len(text))-20
counter = 0

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

QuadgramSetup()

def substitution(text,alphabet):
  OldAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i,char in enumerate(alphabet):
    text = text.replace(OldAlpha[i],char)
  return text


key = copy.deepcopy(alphabet)
#random.shuffle(key)
finished = False
try:
  while finished == False:
      currentDecrypt = ""
      currentFitness = -10000000
      x = 0
      random.shuffle(key)
      while x < 1500:
          #print(x)
          #print(currentFitness)
          choice1 = random.choice(key)
          choice2 = random.choice(key)
          pos1 = key.index(choice1)
          pos2 = key.index(choice2)
          keyNew = copy.deepcopy(key)
          keyNew[pos1] = choice2
          keyNew[pos2] = choice1
          #print(keyNew)

  
          text2 = substitution(text,keyNew)
          text3 = text2.upper()
          fitness = float(GetLikelihood(text3))
          #print(fitness)
          if counter == 1000:
            print(currentFitness)
          #print(currentFitness)
          if fitness <= currentFitness:
              x += 1
          else:
              currentFitness = fitness
              currentDecrypt = text2
              key = keyNew
              x = 0 
              if int(fitness) > int(result):
                  finished = True
                  break
          counter += 1

except:
  pass
print(currentDecrypt)
b = ""
for letter in alphabet:
     b += alphabet[key.index(letter)]
print(b) # Key for substitution ciphers - gives the mapping from plain to cipher 
print(key) #This is more applicable to certain ciphers which make use of substitution such as ADFGVX.