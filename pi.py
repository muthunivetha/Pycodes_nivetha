pi=22.0/7.0




while True:
	p=raw_input("for pi,how many decimal points should be displayed: ")
	if str(p).isdigit():
		
		
		if int(p)>=1 and int(p)<=50:
			
			b='{:.'+ str(p) + 'f}'
			print('PI = '+ b.format(pi))
			break
	
		else:
			print("please enter a number between [1-50]!!")
			continue
		break
		
	else:
		print("invalid input!! input should be numeric!!")
		continue
		
		
