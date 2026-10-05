n = int(input("enter first number: "))
m = int(input("enter second number: "))
i=1
hcf=1
while i <=n and i<=m:
    if n %i ==0 and m%i==0:
        hcf=i
    i+=1
print(hcf)
