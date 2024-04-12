#Bitwise operaters me value  0 ana 1  par kam karata hai
#A and b ake me bhi zero hai to oha zero de deta hai ure two me one hai one deta hai (AND)
#A and b me kisi ake me bhi one hai to oha  one deta hai and two me zero hai to zero deta hai (OR)
# A and b me same value hone par zero deta hai two me zero hai to  zero deta hai and two me one hai to zzero deta hai
x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y))
print(x&y,bin(x&y))
print(bin(x&y),x&y)#1000
print(bin(x|y),x|y)#1010
print(bin(x^y),x^y)#0010

#0b1010
#0b1000
#&_1000___8
#|_1010___10
#^_0010___2

