import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
d=pow(s*(s-a)*(s-b)*(s-c),0.5)
print('%.2f' %d)