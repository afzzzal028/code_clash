n =  int(input("enter a number: "))
a=0
b=1
i=1
while i<=n:
    j=1
    while j<=i:
        print(a, end=" ")
        next_num= a+b
        a=b
        b= next_num
        j+=1
    print()
    i+=1