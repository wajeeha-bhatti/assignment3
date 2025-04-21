# Control Flow
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# While Loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# For Loop
for i in range(5):
    print("Number:", i)

# Break & Continue
for num in range(10):
    if num == 3:
        continue  # skip number 3
    if num == 7:
        break  # stop at number 7
    print(n)
    
    # Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Fruits:", fruits)

# Tuples
coordinates = (10.0, 20.0)
print("X:", coordinates[0])

# Dictionary
person = {
    "name": "Alice",
    "age": 30
}
print("Name:", person["name"])

# Looping through dictionary
for key, value in person.items():
    print(key, ":", value)
//leson7
# Set
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.update([3, 6])  # 3 is already in the set, 6 is added
print("Set:", my_set)

# Removing elements
my_set.discard(2)
print("After discard:", my_set)

# Frozenset
frozen = frozenset([1, 2, 3])
print("Frozen Set:", frozen)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
