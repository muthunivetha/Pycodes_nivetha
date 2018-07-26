class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
	self.radius=radius
        
    def volume(self):
        h,r=self.height,self.radius
	v=3.14*r*r*h
	print("volume : {}" .format(v))
    
    def surface_area(self):
        h,r=self.height,self.radius
	sa=3.14*2*r*h + 2*3.14*r*r
	print("surface area : {}" .format(sa))

c=Cylinder(2,3)
c.volume()
c.surface_area()
