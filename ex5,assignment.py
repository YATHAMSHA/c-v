a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = a

print("a = {0}".format(a))

a += b
print("a += b = {0}".format(a))
a = c

a -= b
print("a -= b = {0}".format(a))
a = c

a *= b
print("a *= b = {0}".format(a))
a = c

a %= b
print("a %= b = {0}".format(a))
a = c

a **= b
print("a **= b = {0}".format(a))
a = c

a //= b
print("a //= b = {0}".format(a))

