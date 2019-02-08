#fahima
a=input().split()
n=int(a[0])
q=int(a[1])
for num in range(n,q):
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
      if sum==num:
           print (num)
