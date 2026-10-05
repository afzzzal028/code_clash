n = int(input("enter a number: "))
orginal=n
armstrong=0
while n>0:
    digit = n%10
    armstrong+= digit **3
    n//=10
if orginal == armstrong:
    print("yes")

else:
    print("no")