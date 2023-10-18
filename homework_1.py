# Homework 1

# Task 1
print(type(None))
print(type(True))
print(type(False))
print(type(1))
print(type(bytearray([1,2,3])))
print(type(5.3))
print(type(5 + 4j))
print(type([1, 5.3, False, 4]))
print(type((1, True, 3, 5+4j)))
print(type(range(5)))
print(type(range(5)))
print(type(' Hello '))
print(type(b'a'))
print(type(bytearray([1,2,3])))
print(type(memoryview(bytearray('XYZ', 'utf-8'))))
print(type({'a', 3, True}))
print(type(frozenset({1, 2, 3})))
print(type({'a': 32}))

# Task 2
def print_smallest(a, b):
    print(min(a, b))

# Task 3
def determine_matching_numbers(a, b, c):
    if a == b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)

# Task 4
def calculate_sum(numbers):
    total_sum = sum(numbers)
    print("Sum of the array:", total_sum)

# Sample array for Task 4
numbers_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Testing Task 2, Task 3, and Task 4
print("\nTask 2:")
print_smallest(10, 5)

print("\nTask 3:")
determine_matching_numbers(10, 20, 10)

print("\nTask 4:")
calculate_sum(numbers_array)
