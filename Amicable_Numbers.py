a=int(input())
b=int(input())
s=0
for i in range(1,a):
    if a%i==0:
        s=s+i
su=0
for j in range(1,b):
    if b%j==0:
        su=su+j
if s==b and su==a:
    print("Amicable")
else:
    print("Not Amicable")