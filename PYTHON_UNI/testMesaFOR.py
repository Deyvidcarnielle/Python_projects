'''s = 0
for i in range(5, 30, 5):
    s += i
print("S =", s)'''


'''s = 0
for i in range(5, 30, 5):
    if i % 2 == 0:
        s += i
print("S =", s)'''

'''b = 2
e = 3
r = 1
for i in range(1, e + 1):
    r *= b
print("R =", r)'''

'''Cálculo de fatorial 
x = 4
r = 1
for i in range(x, 0, -1):
    r *= i
print("R =", r)'''

'''Cálculo de potência
b = 2
e = 3
r = 1
for i in range(1, e + 1):
r *= b
print("R =", r)'''

'''y = 2
x = 1
for i in range(3, 0, -1):
    x *= 2
    if x <= 2:
        y += x
    else:
        y += 2
    msg = "I= {0} Y= {1} X= {2}"
    print(msg.format(i, y, x))'''

y = 2
x = 1
for i in range(3, 0, -1):
    x *= 2;
    if x <= 4:
        y += 2
    else:
        y += x
    msg = "I= {0} Y= {1} X= {2}"
    print(msg.format(i, y, x))