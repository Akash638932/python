class bikeshop:
    def __init__(self,stock):
        self.stock=stock
        def displayBike(self):
            print("Total Bike ,self.stock")
        def rentForBike(self,q):
            
            if q<=0:
                print("Enter the postive value or greater then zero")
            if q>self.stock:
                print("Enter the value(less than stock)")
                
            else:
                print("Total prices",q*100)
                print("Total Bike",self.stock)
                
                
while True:
    obj=bikeshop(100)
    uc=int(input('''
    1 Display stock2
    2 Rent a Bike
    3 Exit
           '''))
    if uc==1:
     obj.DisplayBike()
    elif uc==2:
        n=int(input("Enter the qty:......"))
        obj.rentForBike(n)
    else:
        break