#Tends to be the one used for early transpositons. dcode.fr can be set up to use this method, by parameterising the dropdown for method to be used. Write by row; read by row.
#NON AUTO PROGRAMS NOW DEPRECATED.
from statistics import QuadgramSetup, GetLikelihood
import itertools

text = raw_input("Enter text:").upper()
#keyword = raw_input("enter keyword").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = text.replace(" ","")
text = text.replace(",","")
text = text.replace(":","")
text = text.replace("'","")
text = text.replace(";","")

QuadgramSetup()

keys= []
originalText = text
for count in range(1,10):
    keys = []
    if len(originalText) % count != 0:
        text = originalText + (((((len(originalText) // count) + 1) * count) - len(originalText)) * ".")
    else:
        text = originalText

    for item in itertools.permutations(alphabet[:count], count):
        string = ''.join(item)
        keys.append(string)

    bestPlains = ["","","","",""]
    bestLikelihoods = [-1000000,-1000000,-1000000,-1000000,-1000000]
    bestKeys = ["","","","",""]
    for keyNumber,keyword in enumerate(keys):
        alphKey = ''.join(sorted(keyword))
        rows = int(len(text)/len(keyword))

      
        chars = []
        cols = len(alphKey)
        for i in range(0,len(text),cols):
            chars.append(text[i:i+cols])
        decrypt = [[[] for i in range(len(alphKey))] for j in range(len(chars))]
        

        for i,word in enumerate(chars):
            for j,letter in enumerate(alphKey):
                decrypt[i][keyword.index(letter)] += word[j] 

        Final = ""
        for word in decrypt:
            newWord = ""
            for letter in word:
                newWord += '' . join(letter)
            Final += newWord
                
                
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
    print("Key length",count)
#    print(bestKeys)
#    print(bestPlains)
    print(bestPlains[0])






