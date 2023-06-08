n=int(input())
a=list(map(int,input().split()))
d=sum(a)//len(a)
c=0
for i in a:
    if d>=i:
        c+=1
print(c)