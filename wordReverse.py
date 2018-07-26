def myfunc(s):
	r=''
	l=list(s.split())
	st=l[::-1]
	for i in st:
		r=r+' '+i
	print r

myfunc("iam nivetha from chennai")
