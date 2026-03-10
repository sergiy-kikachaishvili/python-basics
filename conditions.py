# Day 2 - Conditions (if/else)
# Learning Python basics for AI Engineering path

age = 22
salary = 90000
city = "Singen"

# Basic condition
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Multiple conditions
if salary >= 100000:
    print("Senior level salary")
elif salary >= 70000:
    print("Middle level salary")
else:
    print("Junior level salary")

# City condition
if city == "Singen":
    print("Living in Singen")
elif city == "Zurich":
    print("Living in Zurich")
else:
    print("Living in another city")
