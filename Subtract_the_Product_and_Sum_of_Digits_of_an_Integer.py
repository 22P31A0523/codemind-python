n=int(input())
p=1
s=0
q=n
while q!=0:
    r=q%10
    q=q//10
    p=p*r
    s=s+r
    h=p-s
print(h)