def hangman(n):
    y=1
    if n in wo:
        for i in range(len(wo)):
            if wo[i]==n:
                em.insert(i,n)
                em.pop(i+1)
                y=2
    print("\n{} {} {} {} {}".format(em[0],em[1],em[2],em[3],em[4]))
    if wo==em:
        return 1
    if y==1:
        x[0]=x[0]-1
        print(" remaining guess is ",str(x[0]))
    if x[0]==0:
        return 0
    
    

print("you have 10 guesses in total")


wo=['a','p','p','l','e']

em=["_","_","_","_","_"]

print(em[0],em[1],em[2],em[3],em[4])

x=[10]

while True:

    n=input("guess a character : ")

    gue=hangman(n)
    
    if gue==1:
        print("You Won the game")
        break
    if gue==0:
        print("You lost the game")
        break
