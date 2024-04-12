#named indexer:
Txt1="welcome to{Fname}{Iname}".format(Fname="Akash",Iname="gupta")
#numbered indexe:
Txt2="welcome to{0}{1}".format("Akash","gupta")
#empty place holders:
Txt3="welcome to{}{}".format("Akash","gupta")
print(Txt1)
print(Txt2)
print(Txt3)

w="welcome{}to{} Akash".format("hello",20)
print(w)
w="welcome {a}to{b}Akash".format(a=30,b=40)
print(w)