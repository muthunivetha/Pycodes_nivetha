import random


def dice():

	
	while True:
		min=input("enter min range:")
		max=input("enter max range:")

		x=random.randint(min,max)
	
		print(int(x))
	
		x=raw_input("do you want to choose again:[y/n]")
		
		if x=='y':
			continue
		elif x=='n':
			break
		else:
			print("wrong input")

	


print("*****Dice Rolling Simulator*****\n")

dice()
