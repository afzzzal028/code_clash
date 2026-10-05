n=int(input("enter a number: "))
i=1
total=0
while i<n:
    if n%i==0:
        total+=i
    i+=1
if total==n:
    print("yes")
else:
    print("no1")