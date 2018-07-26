def display_board(board):
	
	print(  " " + board[1] + " | " + board[2]  + " | "  + board[3])
	print( "----------")
	print(  " " + board[4] + " | " + board[5]  + " | "  + board[6])
	print( "----------")
	print(  " " + board[7] + " | " + board[8]  + " | "  + board[9])

def player_input():

	while True:
	
		a= raw_input("player 1: choose your symbol [x/o] : ")
	
		st=['x','o']
		global p1
		global p2
		p1=''
		p2=''
		if a == 'x':
			p1=p1+a
			p2=p2+st[1]
			print("player 1 is : {}" .format(p1))
			print("player 2 is : {}" .format(p2))
			break
		elif a == 'o':
			p1=p1+a
			p2=p2+st[0]
			print("player 1 is : {}" .format(p1))
			print("player 2 is : {}" .format(p2))
			break
		
		else:
			print("wrong input!! choose between 2 symbols [x/o]!  ")
			continue

		
def players(board):
	print("iam from player function:")


	while True:

		while True:
	
			pla1=int(input("player 1: enter yur choice of position : "))

			if board[pla1]=='':
				board[pla1]=p1
				break
			else:
				print("entered position is occupied!!")
				print("choose someother position other than {} ".format(pla1))
				continue
		display_board(board)

		if board[1]=='x' and board[2]=='x' and board[3]=='x':
			print(board[1] ,"wins !!")
			break
		if board[4]=='x' and board[5]=='x' and board[6]=='x':
			print(board[4] ,"wins !!")
			break
		if board[7]=='x' and board[8]=='x' and board[9]=='x':
			print(board[7] ,"wins !!")
			break
		if board[1]=='x' and board[4]=='x' and board[7]=='x' :
			print(board[1] ,"wins !!")
			break
		if board[2]=='x' and board[5]=='x' and board[8]=='x':
			print(board[2] ,"wins !!")
			break
		if board[3]=='x' and board[6]=='x' and board[9]=='x':
			print(board[3] ,"wins !!")
			break
		if board[1]=='x' and board[5]=='x' and board[9]=='x' :
			print(board[1] ,"wins !!")
			break
		if board[3]=='x' and board[5]== 'x' and board[7]=='x':
			print(board[3] ,"wins !!")
			break
		if board[1]=='o' and board[2]=='o' and board[3]=='o':
			print(board[1] ,"wins !!")
			break
		if board[4]=='o' and board[5]=='o' and board[6]=='o':
			print(board[4] ,"wins !!")
			break
		if board[7]=='o' and board[8]=='o' and board[9]=='o':
			print(board[7] ,"wins !!")
			break
		if board[1]=='o' and board[4]=='o' and board[7]=='o' :
			print(board[1] ,"wins !!")
			break
		if board[2]=='o' and board[5]=='o' and board[8]=='o':
			print(board[2] ,"wins !!")
			break
		if board[3]=='o' and board[6]=='o' and board[9]=='o':
			print(board[3] ,"wins !!")
			break
		if board[1]=='o' and board[5]=='o' and board[9]=='o' :
			print(board[1] ,"wins !!")
			break
		if board[3]=='o' and board[5]== 'o' and board[7]=='o':
			print(board[3] ,"wins !!")
			break

		while True:
	
			pla2=int(input("player 2: enter yur choice of position : "))

			if board[pla2]=='':
				board[pla2]=p2
				break
			else:
				print("entered position is occupied!!")
				print("choose someother position other than {} ".format(pla2))
				continue
		display_board(board)
		continue

print("Welcome to the Tic Tac Toe game!!! \n")
board=['#','','','','','','','','','','']

display_board(board)
player_input()
players(board)









