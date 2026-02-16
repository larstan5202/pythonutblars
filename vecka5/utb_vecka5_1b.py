# Ekvivalentklasser för uttrycket y == 42

print("Uttryck: y == 42")
print("Ekvivalentklasser: ")

print("1. y == 42 (sant)")
print("   Exempel: 42")

print("2,  y != 42 (falskt)")
print("    Exempel: 0, 10, 41, 43, 100")

# Lägger till en inmatningsdel

y = int(input("Skriv ett tal:  "))

if y == 42:
    print("Talet tillhör ekvivalentklassen: y == 42 (sant)")
else:
    print("Talet tillhör ekvivalensklassen: y != 42 (falskt)")

