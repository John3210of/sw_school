
# global, nonlocal
b=0
def f():
    a = 20
    global b
    b = a
b=15
f()
print(b)
