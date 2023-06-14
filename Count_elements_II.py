n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
c=0
d=[]
for i in a:
    if i not in b:
        if i not in d:
            d.append(i)
            s+=1
for i in b:
    if i not in a:
        if i not in d:
            d.append(i)
            c+=1
print(s+c)