import random


def guess(min,max):
	for i in range(min,max):
		x=random.randint(min,max)

	
	while True:

		a=input("guess the number:")
		if a==x:
			print("congrats!! your guess {} and the random number {} are same!!".format(a,x))
			break
		elif a>x:
			print("your guess is higher than the random number!")
			continue
		elif a<x:
			print("your guess is lesser than the random number!")
			continue
		else:
			print("wrong input")

		


print("*****Guess the Number*****\n")

min=input("enter min range:")
max=input("enter max range:")
guess(min,max)
