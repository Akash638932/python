l=[10,20,30,40,50,60]
print(len(l))
s="string"
print(len(s))

##overloding
class ag:
    def displayeinfo(self,name=''):
        print("welcome to Akash"+name)
        
obj=ag()
obj.displayeinfo()
obj.displayeinfo('aditya')#overloding

##overriding
class ag:
    def displayeinfo(self):
        print("welcome to Akash")
        
        
class IIT(ag):
    def displayeinfo(self):
        super().displayeinfo()
        print("welcome to IIT")
        
obj=IIT()
obj.displayeinfo()