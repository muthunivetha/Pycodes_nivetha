n=input("enter the no of terms in the fibo sequence:")

f=0
s=1

for i in range(n+1):
	if i<=1:
		ne=i
	else:
		ne=f+s
		f=s
		s=ne
	print(ne)
		
