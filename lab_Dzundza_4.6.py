import math
p = 15
k = 1
i = 1
z1 = 0
z2 = 1

while k != p+1:
    while i != k+1:
        sum = math.cos(i+k)
        z1 += sum
        i += 1

    z2 *= math.pow(z1+1, 2)
    k += 1
    z1 = 0
    i = 1