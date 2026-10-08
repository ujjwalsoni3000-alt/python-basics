def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Asha"))
print(greet("Ravi", "Namaste"))

def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4))
