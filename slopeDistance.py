import math

class Line:
    
    def __init__(self,coor1,coor2):
        print("computation of slope and distance started!!")
	self.coor1=coor1
	self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
	x2,y2=self.coor2
	
	x= (x2-x1)**2
	y= (y2-y1)**2
	z=(x+y)**0.5

	print("distance : {} ".format(z))
    
    def slope(self):
	x1,y1=self.coor1
	x2,y2=self.coor2
        print ( "slope : {}"  .format(float (y2-y1) / (x2-x1)))

p=Line((3,2),(8,10))

p.distance()
p.slope()


