import math
from prettytable import PrettyTable

x1 = float(input("x початкове:"))
x2 = float(input("x кінцеве:"))
x3 = float(input("x проміжне:"))

yy= ['Y']
xx = ['X']

while x1 != x2:
    k = 5*math.pow(math.e, (3*x1))

    if x1 <= -1:
        k1 = (3+math.sin(math.fabs(x1)))
        y = k-k1
        yy.append(y)
    elif -1 <= x1 and x1 <= 3:
        k2 = (2*math.pow(math.e, (x1/4-1)))
        y = k-k2
        yy.append(y)
    elif x1 > 3:
        k3 = (7-math.sqrt(2*int(x1)^3))
        y = k-k3
        yy.append(y)
    
    xx.append(x1)
    x1 = x1 + x3

st = len(yy)
table = PrettyTable(xx)

while yy:
    table.add_row(yy[:st])
    yy = yy[st:]

print(table)

input()