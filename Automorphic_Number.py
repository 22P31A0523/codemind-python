n=int(input())
l=len(str(n))
s=n**2
r=s%pow(10,l)
s/=10
if r==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")