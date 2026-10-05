n= int(input("enter a number: "))

i=2
while i <=n:
    j=2
    is_prime=True
    while j<i:
        if i%j==0:
            is_prime= False
            break
        j+=1
    if is_prime:
        print(i)
    i+=1