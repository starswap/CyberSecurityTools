#Simple frequency analysis with percentages
#----To Add Bigram and trigram analysis--- Use http://www.richkni.co.uk/php/crypta/freq.php
from utilities import InputText
text = InputText()
text1 = text.lower()
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
percentages = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
results = []

for i in range (0,len(letters)):
	while True:
		var = text1.find(letters[i],0,len(text))
		if not( var == -1):
			text1 = text1[:var] + "" + text1[var + 1:]
			frequencies[i] += 1
		else:
			break
for i in range(0,len(letters)):
	print(letters[i]+":"+str(frequencies[i]))

for i in range(0,len(letters)):
	percent = frequencies[i]/float(len(text))
	percentages[i] = percent
	
	if i == 0:
		results = [[letters[i],percent]]
	else:
		inserted = False
		for j in range(0,len(results)):
		
				if percent < results[j][1]:
					continue
				else:
					results.insert(j,[letters[i],percent])
					inserted = True
					break
		
		if inserted == False:
			results.append([letters[i],percent])
			inserted = True

for i in range(0,len(letters)):	
	print(str(results[i][0]) + ":" +str(results[i][1]))

print(''.join([elem[0] for elem in results]))