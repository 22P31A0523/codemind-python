n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,n):
    if i%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
se=sum(e)
so=sum(o)
s=abs(se-so)
if s%4==0:
    print('X')
else:
    print('Y')