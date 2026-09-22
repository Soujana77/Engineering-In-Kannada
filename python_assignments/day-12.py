#Homework
'''
1.List Manipulation:
Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

2.Sum of Prices:
Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

3.List of Squares:
Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

4.Student Data Task:
Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.

5.Dictionary Comprehension:
Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.

6.Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:
Prints the entire matrix row by row.
Prints the sum of each row in the matrix.
Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''

#1.List Manipulation:
foods = ["Dosa", "Idli", "Bisi Bele Bath", "Ragi Mudde", "Vada"]

upper_foods = [food.upper() for food in foods]

print("Original list:", foods)
print("Uppercase list:", upper_foods)

#2.Sum of Prices:
items = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 40,
    "Biscuits": 25
}

total = 0

for price in items.values():
    total = total + price

print("Total price:", total)

#3.List of Squares:
numbers = list(range(1, 11))

squares = [number ** 2 for number in numbers]

print("Numbers:", numbers)
print("Squares:", squares)

#4.Student Data Task:
students = [
    {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    {
        "name": "Priya",
        "age": 21,
        "marks": 92
    },
    {
        "name": "Arjun",
        "age": 20,
        "marks": 78
    }
]

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Marks:", student["marks"])
    print()

#5.Dictionary Comprehension:
cities = {
    "Bengaluru": 13600000,
    "Mysuru": 1000000,
    "Mangaluru": 700000,
    "Hubballi": 950000,
    "Belagavi": 800000,
    "Davanagere": 600000
}

filtered_cities = {
    city: population
    for city, population in cities.items()
    if population >= 1000000
}

print("Cities with population 10 lakhs or more:")
print(filtered_cities)

#6.Nested List Challenge:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")

for row in matrix:
    print(row)

print("Sum of each row:")

for row in matrix:
    total = 0

    for number in row:
        total = total + number

    print(total)