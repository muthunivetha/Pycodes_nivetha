def myfunc(s):
	l=list(s.split())
	p=''
	if len(l)==2:
		for i in l:
			p=p+i[0]
		li=list(p)
		if li[0]==li[1]:
			print True
		else:
			print False
			
	else:
		print("it is not a 2-word string")
	

myfunc('hi hivetha')
