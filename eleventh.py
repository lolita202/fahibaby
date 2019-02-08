a=input().split()
n=int(a[0])
k=int (a[1])
pow=n**k
print(pow)

On Fri, 8 Feb 2019 at 10:00, manoj maxx <manojd60365@gmail.com> wrote:
sum=0
x=input().split()
y=input().split()
n=int(x[0])
k=int(x[1])
for j in range(0,k):
  sum=sum+int(y[j])
print(sum)

On Fri, 8 Feb 2019 at 09:36, manoj maxx <manojd60365@gmail.com> wrote:
c=0

a=int(input())
while(a>0):
  a=a//10
  c=c+1
print(c)
