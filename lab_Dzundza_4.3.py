from prettytable import PrettyTable

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

yy = ["Y"]
xx = ["X"]

x = int(input(" x початкове: "))
x2 = int(input(" x кінцеве: "))
dx = int(input(" x проміжкове: "))

while x <= x2:
    if c < 0 and b != 0:
        y = a*x^2+b^2*x
        yy.append(y)
    elif c > 0 and b == 0:
        y = (x+a)/(x+c)
        yy.append(y)
    else:
        y = x/c
        yy.append(y)

    xx.append(x)
    x += dx

st = len(xx)
table = PrettyTable(xx)

while yy:
    table.add_row(yy[:st])
    yy = yy[st:]

print(table)