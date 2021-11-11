text = raw_input("Enter text:").upper()
text = text.replace(" ","")
for rails in range(2,20):
  decrypt = [" " for i in range(len(text))]
  posn = 0
  iters = 0
  deltas = []
  delta = 2*(rails-1)
  for char in text:
    deltas.append(delta)
    delta -= 2
    if (delta == 0):
      delta = 2*(rails-1)

  for i,char in enumerate(text):
    #print(decrypt)
    decrypt[posn] = char
    posn += deltas[posn]

    if posn >= len(text):
      iters += 1
      posn = iters
      
  print("Number of rails",rails)
  print(''.join(decrypt))