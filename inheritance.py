class A:#single inharitance
    def displayA(self):
      print("welcome to Akash A")
      
class B(A):
    
    def displayB(self):
        print("welcome to Akash B")
obj=B()
obj.displayA()
obj.displayB()
print("single inharitance")

print( )

#multilevel inharitance
class A:
    def displayA(self):
      print("welcome to Akash A")
      
class B(A):
    
    def displayB(self):
        print("welcome to Akash B")
class C(B):
   def displayC(self):
        print("welcome to Akash C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
print("multilevel inharitance")

print( )

#multiple inharitance
class A:
    def displayA(self):
      print("welcome to Akash A")
      
class B:
    
    def displayB(self):
        print("welcome to Akash B")
class C(A,B):
   def displayC(self):
        print("welcome to Akash C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
print("multiple inharitance")



