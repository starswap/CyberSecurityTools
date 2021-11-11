#Based on https://github.com/ITAYC0HEN/XOR-Files/blob/master/xor.py
import sys
filel_b = bytearray(open(sys.argv[1],srbs).read())
crib = "INSERT CRIB HERE" 
size = len(filel_b)
xord_byte_array = bytearray(size)
for key in range(255): #Only one byte keys for now
  k = key.to_bytes(1,'big')
  for i in range(len(filel_b)):
    j = i
    i %= len(filel_b)
    j %= len(k) 
   
    xord_byte_array[max(i,j)] = filel_b[i]^k[j] 
  open("ka","wb").write(xord_byte_array)
  t = open("ka","rb").read()
  print(key,end=" ")
  if bytes(crib,'ascii') in t:
    print("Yes")
  else:
    print("No")
