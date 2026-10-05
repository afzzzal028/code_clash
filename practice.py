"""
i=1
while i<=10:
    j=1
    while j<=10:
        print(i,  "x", j, "=", i*j)
        j+=1
    print()
    i+=1
"""

"""n = int(input("enter a number: "))
i=1
while i<=n:
    j=1
    while j<=n:
        print("(",i,j,")")
        j+=1
    print()
    i+=1
    """

"""n=5
i=n
while i>=1:
    j=i
    while j>=1:
        print(j, end=" ")
        j-=1
    print()
    i-=1
    """
"""
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    """
"""n=int(input("enter a number: "))
original = n
reversed = 0
while n>0:
    digit=n%10
    reversed= reversed*10+ digit
    n//=10
if original==reversed:
    print("yes")
else:
    print("no")
    """

arr= [1,1,2,3,3,2,3,1,3,2]
freq={}
for x in arr:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
print(freq)