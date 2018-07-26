n=int(input("enter the number"))

l=[2,3,4,5,6,7,8,9]

p=[]
for i in l:
	if n%i==0:
		p.append(i)
		#print(i)


print(p)
while n%2==0:
        print 2,
        n=n/2
for u in p:
	
	while n%u==0:
		print(u)
		n=n/u
		break
	

if n>2:
        print(n)			


	
			


		
			
	
			
		
