#operators :Operators are special symbols or keywords that perform operations on variables and values.
#Arithmetic   : `+`, `-`, `*`, `/` 
#| Comparison : `==`, `!=`, `<`    
#| Assignment : `=`, `+=`, `-=`    
#| Logical    : `and`, `or`, `not` 
#| Bitwise    : & , | , ^ , ~ , << , >> 
#| Membership : `in`, `not in`     |               |
#| Identity   : `is`, `is not`                   

# Demonstrate all Python operators in one simple program

print("=== 1. Arithmetic Operators ===")
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

print("\n=== 2. Comparison (Relational) Operators ===")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

print("\n=== 3. Assignment Operators ===")
x = 5
print("Initial x =", x)
x += 2
print("x += 2 =>", x)
x -= 1
print("x -= 1 =>", x)
x *= 3
print("x *= 3 =>", x)
x /= 2
print("x /= 2 =>", x)
x %= 4
print("x %= 4 =>", x)
x **= 2
print("x **= 2 =>", x)
x //= 2
print("x //= 2 =>", x)

print("\n=== 4. Logical Operators ===")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\n=== 5. Bitwise Operators ===")
m = 6       # 110 in binary
n = 3       # 011 in binary
print("m & n:", m & n)     # 2
print("m | n:", m | n)     # 7
print("m ^ n:", m ^ n)     # 5
print("~m:", ~m)           # -7
print("m << 1:", m << 1)   # 12
print("m >> 1:", m >> 1)   # 3

print("\n=== 6. Membership Operators ===")
lst = [1, 2, 3, 4]
print("2 in lst:", 2 in lst)
print("5 not in lst:", 5 not in lst)

print("\n=== 7. Identity Operators ===")
a = [1, 2]
b = a
c = [1, 2]
print("a is b:", a is b)
print("a is c:", a is c)
print("a == c (value equality):", a == c)
print("a is not c:", a is not c)

