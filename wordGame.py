word=raw_input("enter a word")

q=word[0]


if q in 'aeiou':
	for i in word:
		x= i + 'ay'
else:
	
	x= word[1:]+ word[0]+ 'ay'

print(x)
