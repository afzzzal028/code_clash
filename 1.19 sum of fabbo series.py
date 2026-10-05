n=int(input("Enter a number: "))
a=0
b=1
i=1
total=0
while i<=n:
    total+=a
    next_num= a+b
    a=b
    b=next_num
    i+=1

print(total)