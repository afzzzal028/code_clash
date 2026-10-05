n= int(input("enter a number"))
i=1
while i<=n:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    print(i,"->",count)
    i+=1