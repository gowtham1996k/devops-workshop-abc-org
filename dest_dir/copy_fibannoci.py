nterms = int(input("How many terms?"))

n1, n2 = 0, 1
for i in range(nterms):
	print(n1)
	nth = n1 + n2
	n1=n2
	n2=nth
print("This line should be the difference")
