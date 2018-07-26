import math




while True:
	p=raw_input("for e ,how many decimal points should be displayed: ")
	if str(p).isdigit():
		
		
		if int(p)>=1 and int(p)<=50:
			
			b='{:.'+ str(p) + 'f}'
			print('e = '+ b.format(math.e))
			break
	
		else:
			print("please enter a number between [1-50]!!")
			continue
		break
		
	else:
		print("invalid input!! input should be numeric!!")
		continue
		
		
