#fahima
n=int(input())
N=n
rev=0
while (n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(N==rev):
    print("yes")
else:
    print("no")
