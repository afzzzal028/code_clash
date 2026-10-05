n=int(input("Enter a number: "))
i=0
while n>0:
    digit = n%10
    i+=digit
    n//=10

print(i)
