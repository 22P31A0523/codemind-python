n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    c=sum(b)
print(c)