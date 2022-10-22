import math
from prettytable import PrettyTable

x = int(input("x початкове: "))
x2 = int(input("x кінцеве: "))
dx = int(input("x проміжне: "))
R = float(input('R='))

xx = ['X']
yy = ['Y']

while x <= x2:
    if x <= -5:
        y = -3
        yy.append(round(y, 1))
    elif x > -5 and x <= -R:
        y = 1.5*(x+3)
        yy.append(round(y, 1))
    elif x > -R and x <= R:
        R2 = math.pow(R, 2)
        X2 = math.pow(x, 2)
        y = math.sqrt(R2-X2)
        yy.append(round(y, 1))
    elif x > R and x <= 8:
        y = (x-3)/2.5
        yy.append(round(y, 1))
    elif x > 8:
        y = R
        yy.append(round(y, 1))
    else:
        y = 'Число не входить в область визначення'

    xx.append(x)
    x += dx

st = len(yy)
table = PrettyTable(xx)

while yy:
    table.add_row(yy[:st])
    yy = yy[st:]

print(table)
input()