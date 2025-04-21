a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor division: 3
x = 5
x += 3  # x = x + 3 → 8
x -= 2  # x = x - 2 → 6
x *= 2  # x = x * 2 → 12
x /= 3  # x = x / 3 → 4.0
x %= 3  # x = x % 3 → 1.0
x **= 2 # x = x ** 2 → 1.0
x //= 2 # x = x // 2 → 0.0
a = 5
b = 7

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
a = True
b = False

print(a and b) # False
print(a or b)  # True
print(not a)   # False
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)   # True (same object)
print(x is z)   # False (different objects, same content)
print(x is not z) # True
my_list = [1, 2, 3, 4]

print(2 in my_list)     # True
print(5 not in my_list) # True
a = 5      # 0101
b = 3      # 0011

print(a & b)  # AND: 1 (0001)
print(a | b)  # OR: 7 (0111)
print(a ^ b)  # XOR: 6 (0110)
print(~a)     # NOT: -6
print(a << 1) # Left shift: 10 (1010)
print(a >> 1) # Right shift: 2 (0010)
