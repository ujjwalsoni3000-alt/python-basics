nums = [3, 1, 2]
nums.append(4)
nums.sort()
print(nums)

point = (10, 20)
print(point[0])

student = {"name": "Asha", "age": 20}
student["grade"] = "A"
for key, value in student.items():
    print(key, value)

unique = set([1, 1, 2, 3, 3])
print(unique)

# List comprehension
squares = [n ** 2 for n in range(1, 6)]
print(squares)
