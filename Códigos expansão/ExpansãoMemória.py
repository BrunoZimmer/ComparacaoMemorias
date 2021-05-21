# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newlines mode (deprecated)

file = "C:/Users/Bruno/Desktop/IC-2021/Python/output.txt"
f = open(file, "w")

#Elementos = int(input("Quantos elementos vai ter a matriz?"))
Elementos = 9
# WordLines = int(input("Quantos WordLines?"))
for i in range(1, Elementos+1,1):
    print('real Corrente'+ str(i) +' = I(Vtest'+ str(i) + ')', file=open(file, "a"))