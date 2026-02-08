import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


# Let's explore interactive mode
name = "Python Learner"
print(f"Hello, {name}!")

# Some data to work with
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Calculate something
total = sum(numbers)
print(f"Total: {total}")

# iterations
count = 14
for i in range(1, count, 2):
    print(f"{i}")

for letter in "abc":
    print(f"{letter}")


# data structures
list0 = ["Name", "Surname", "Age"]

tuple0 = ("Xyz", 14, False)

set0_0 = {1, 1, 3}
set0_1 = ["Xyz", 14, False, False, 14, 15]

dict0 = {"Name": "Xyz", "Age": 14, "Eligible": False}

# list
list1 = ["Name", "Surname", "Age"]
list2 = [1, "Name", True, 1.1]

for element in list1:
    print(f"{element}")
for element in list2:
    print(f"{type(element)}")
    print(f"{element}")

print(f"{type(list1)}")

# dic

dict1 = {"Name": "Xyz", "Age": 14, "Eligible": False}

print(f"{type(dict1)}")

for element in dict1:
    print(f"{type(element)}")
    print(f"{element}")

# tuple

tuple1 = ("Xyz", 14, False)

for element in tuple1:
    print(f"{type(element)}")
    print(f"{element}")

print(f"{type(tuple1)}")

# set
set1 = {1, 1, 3}

for element in set1:
    print(f"{type(element)}")
    print(f"{element}")

print(f"{type(set1)}")

set2 = ["Xyz", 14, False, False, 14, 15]

for element in set2:
    print(f"{type(element)}")
    print(f"{element}")

print(f"{type(2)}")
