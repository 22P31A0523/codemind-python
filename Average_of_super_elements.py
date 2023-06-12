n=int(input())
l=list(map(int,input().split()))
a=[]
s=0
for i in l:
    if i==l.count(i):
        if i not in a:
            a.append(i)
            s=s+i
if s>0:
    b=s/len(a)
    print("%.2f" %b)
else:
    print("-1")