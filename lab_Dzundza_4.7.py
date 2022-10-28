import math
from prettytable import PrettyTable

x1 = float(input('X початкове: '))
x2 = float(input('X кінцеве: '))
dx = float(input('інтервал X: '))
#e = int(input('похибка: '))
xx = ["X"]
yy = ["Y"]
tmp = 1
q = 1
yk = ["Sum"]

if x1 >= -1 and x1 < 1:
    while x1 != x2+dx:
        xx.append(round(x1,3))
        pow = math.pow(x1, tmp)
        q *= pow
        yk.append(round(q, 3))
        yy.append(round(pow, 3))
        x1 += dx
        tmp += 1
else:
    print('X не входить в межі -1<=x<1')

gg = math.log(1-q)

st = len(yy)
table = PrettyTable(xx)

while yy:
    table.add_row(yy[:st])
    yy = yy[st:]

while yk:
    table.add_row(yk[:st])
    yk = yk[st:]

print(table)
a = input()