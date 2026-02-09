a = 5
def fun3(a):
    a += 1
a += 2
print(a)

# Anropa funktionen  så den returnerar ett nytt värede.

a = 5
def fun3(a):
    return a + 1
a = fun3(a)
a += 2
print(a)
