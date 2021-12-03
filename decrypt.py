from sys import argv

cheie = argv[1]
fisierin = argv[2]
fisierout= argv[3]
f= open( fisierin )
sir= f.read()

sirout=""
for index in range (len(sir)):
	ch= chr( ord(sir[index])^ ord(cheie[index % len(cheie)]))
	sirout=sirout+ ch

f= open( fisierout , "w")
f.write(sirout)
f.close()
