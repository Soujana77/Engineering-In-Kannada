#Homework
'''
1.Multiples of 3:
Write a for loop that prints all multiples of 3 between 1 and 30.

2.Sum of First 10 Numbers:
Write a program using a for loop that calculates the sum of numbers from 1 to 10.

3.Print Your Name Letter by Letter:
Write a program that takes your name as input and prints each letter of your name using a for loop.

4.Count Vowels in a String:
Write a program that counts how many vowels are in a given string using a for loop.

'''
#1.Multiples of 3:
for i in range(3, 31, 3):
    print(i)

#2.Sum of First 10 Numbers:
sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum:", sum)    

#3.Print Your Name Letter by Letter:
name = input("Enter your name: ")

for letter in name:
    print(letter)

#4.Count Vowels in a String:
text = input("Enter a string: ")

count = 0

for letter in text:
    if letter.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)    