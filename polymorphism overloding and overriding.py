##overloding
class Area:## polymorphism adhik use hota hai
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:#dono me value likhe rahi hai
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing found!")
obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)
print("overloding")

print( )

##overriding

class A:## inharitance me adhik use hota hai
    def showdata(self):
        print("I m in A class")
        
class B(A):
    def showdata(self):
        print("I m in B class")
        
obj=B()
obj.showdata()

