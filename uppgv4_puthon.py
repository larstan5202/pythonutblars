# 1a egentligen inget fel men den använder inte parametern t, ändra i print till ("t")

def foo(t):
    #print("test")
    print(t)

foo("hej")

# 1b fel anrop i anropet anropar ej fun1.

def fun1(x, y):
    return x * y
print(fun1(3, 5))

# 1c

def fun1(x, y):
    return x * y
print(fun1(1, 2))

# 1d

def fun2(i):
    return 5 * i
x = 2
y = 3
a = fun2((x) + fun2(y))
print(a)
# denna fungerade inte, jag fick skapa en ny fil där det fungerade.




