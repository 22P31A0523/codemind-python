import math
n=int(input())
s=math.sqrt(n)
if int(s + 0.5) ** 2 == n:
    print(True)
else:
    print(False)