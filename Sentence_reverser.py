Input = input("Enter a sentence: ")
new = Input.replace(".",  " ")	#replacing . with space.
lzt = new.split(" ")	#splitting the string and making it a list.

for i in lzt:
	print(i[::-1]," ", end = "")	#reversing every words one by one and printing them in a single line.
print()