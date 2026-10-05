n=int(input("enter a number: "))
i=1
factorial=1
while i<=n:
    factorial *=i #could be written as factorial = factorial*i
    i+=1
print(factorial)