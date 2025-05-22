def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def print_uppercase_names(names):
    for name in names:
        print(name.uppercase())  # ❌ AttributeError: 'str' object has no attribute 'uppercase'

def divide_numbers(a, b):
    return a / b  # ❌ Might cause ZeroDivisionError if b == 0

def find_element_index(elements, target):
    return elements.index(target)  # ❌ ValueError if target is not in list

# Sample usage
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average)

names = ["Alice", "Bob", "Charlie"]
print_uppercase_names(names)

print("Division:", divide_numbers(100, 0))  # ❌ Division by zero

elements = [1, 2, 3, 4, 5]
print("Index of 10:", find_element_index(elements, 10))  # ❌ 10 is not in the list
