from statistics import ioc, ChiSquared
from utilities import InputText
text = InputText().upper()
text = text.replace(" ","")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
iocs = [0]  

for key in range(2,15):
  texts = []
  for i in range(key):
    texts.append("")
  for i,char in enumerate(text):
    texts[i % key] += char
  avgs = []
  for t in texts:
    avgs.append( ioc(t))
  #print(avgs)
  total = 0
  for a in avgs:
    total += a
  avg = total/float(len(avgs))
  iocs.append(avg)
for i,item in enumerate(iocs):
  print(str(i+1) + ": " +str(item))

greatest = 0
for i,k in enumerate(iocs):
  if k > greatest:
    greatest = k
    key = i +1
print(key)
caesars = []
for i in range(key):
  caesars.append("")
for i,char in enumerate(text):
  caesars[i % key] += char

shifts = []
cracked = []
for caesar in caesars:
  bestShift = 0
  thisround = []
  for shift in range (1,27):
    newstring = ""
    for letter in caesar:
      num = alphabet.index(letter)
      num = num + shift
      newstring += alphabet[num % 26]
    thisround.append(newstring)
    newstring = ""
  result = ""
  lowest = 100000
  
  for p,string in enumerate(thisround):
    if ChiSquared(string) < lowest:
      lowest = ChiSquared(string)
      result = string
      bestShift = alphabet[25-(p)]
  
  cracked.append(result)
  shifts.append(bestShift)

solution = ""
for i,char in enumerate(cracked[0]):
  solution += char
  for crack in cracked[1:]:
    try:
      solution += crack[i]
    except IndexError:
      pass
print(solution)
print(shifts)
