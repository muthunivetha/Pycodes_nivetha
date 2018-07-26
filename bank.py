class Bank():
	

	def __init__(self,owner,balance):
		self.owner=owner
		self.balance=balance	

	def deposit(self,a):
		self.a=a
		
		self.balance=self.balance+a
		print("total money after deposit = {}" .format(self.balance))

	def withdrawl(self,b):
		self.b=b
		self.balance=self.balance-b
		print("total money after withdrawl = {}" .format(self.balance))

bank=Bank('nive',500)
bank.deposit(300)
bank.withdrawl(200)

