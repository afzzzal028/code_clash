n = int(input("enter a number: "))
i=1
total=0
while i<=n:
    if n%i==0:
        total+=i
    i+=1
print(total)
