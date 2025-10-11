print('------------------------------------------------------------')
# Exercise 1: Count Up with range(stop)
# Print the numbers 0 to 9 
# Use: range(10)
# Bonus Challenge: Print on one line, separated by spaces.

# Example: Output = 0 1 2 3 4 5 6 7 8 9

for x in range(10):
  print(x, end=' ')

print('\n')
print("------------------------------------------------------------")

# Exercise 2: Count Down with range(start, stop, step)
# Print 10 down to 1 
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 10 9 8 7 6 5 4 3 2 1

for x in range(10,0,-1):
  print(x,end=' ')

print('\n')
print("------------------------------------------------------------")

# Exercise 3: Evens in a Range
# Print all even numbers from 2 to 20.
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 2 4 6 8 10 12 14 16 18 20

for x in range(2,21,2):
  print(x,end=' ')

print('\n')
print("------------------------------------------------------------")

# Exercise 4: Multiples with Steps
# Print the first 6 multiples of 9.
# Use: range(start, stop, step) where step = 9
# Tip: Think about where to stop so you get 6 numbers.
# Example: Output = 9 18 27 36 45 54

for x in range(9,55,9):
  print(x,end=' ')

print('\n')
print("------------------------------------------------------------")

# Exercise 5: Running Total (Accumulator)
# Compute the sum of all integers from 1 to 100 (inclusive) and print it.
# Use: range(1, 101)
# Example: Output = 5050
counter = 0
for x in range(1,101):
  counter = counter + int(x)
print(counter)

print('\n')
print("------------------------------------------------------------")

# Exercise 6: Sum of Multiples
# Compute the sum of multiples of 3 from 3 to 30 (inclusive).
# Use: range(3, 31, 3)
# Example: Output = 165
count = 0
for x in range(3,31,3):
  count = count + int(x)
print(count)

print('\n')
print("------------------------------------------------------------")

# Exercise 7: Loop Through a String (characters)
# Count the vowels in the string and print the total.
# Data:
# text = "Computhink Academy"
# Vowels: a, e, i, o, u (case-insensitive)
# Example: Output = 7

text =  "Computhink Academy"
vcount = 0
for x in text:
  if x.lower() in ['a','e','i','o','u']:
    vcount += 1
print(vcount)

print('\n')
print("------------------------------------------------------------")

# Exercise 8: Loop Through a String Using Index
# Print each character with its index in the format: index:char
# Data:
# name = "Python"
# Example: 
# 0:P
# 1:y
# 2:t
# 3:h
# 4:o
# 5:n
name = 'Python'
count = 0
for x in name:
  print(count, x)
  count += 1

print('\n')
print("------------------------------------------------------------")

# Exercise 9: Every 2nd Character (Index Step)
# Print every 2nd character (positions 0, 2, 4, ...) of the string on one line (no spaces).
# Data:
# s = "abcdefghijkl"
# Example: Output = acegik

s = "abcdefghijkl"
result = ''
result += s[::2]
print(result)

print('\n')
print("------------------------------------------------------------")

# Exercise 10: Loop Through a List (values)
# Print the squares of all numbers in the list on one line, separated by spaces.
# Data:
# nums = [3, 1, 4, 1, 5, 9]
# Example: Output = 9 1 16 1 25 81

nums = [3, 1, 4, 1, 5, 9]
for x in nums:
  print(x**2, end=" ")

print('\n')
print("------------------------------------------------------------")

# Exercise 11: Loop Through a List Using Index
# Replace every negative number in the list with 0, then print the updated list.
# Data:
# data = [5, -2, 7, -9, 0, 4]
# Expected final list: [5, 0, 7, 0, 0, 4]

data = [5, -2, 7, -9, 0, 4]
for x in range(len(data)):
  if data[x] < 0:
    data[x] = 0
print(data, end=" ")

print('\n')
print("------------------------------------------------------------")


# Exercise 12: Manual Max (No max())
# Find and print the largest number in the list without using max().
# Data:
# scores = [42, 67, 23, 88, 55, 88, 12]
# Example: Output = 88

scores = [42, 67, 23, 88, 55, 88, 12]
highest = scores[0]
for x in scores:
  if x > highest: 
    highest = x 
print(highest)

print('\n')
print("------------------------------------------------------------")

# Exercise 13: Loop through a List (index + value)
# Print each item with a 1-based index like "1) apple", "2) banana", ...
# Data:
# fruits = ["apple", "banana", "cherry", "durian"]

fruits = ["apple", "banana", "cherry", "durian"]
index = 0
for x in fruits:
  index += 1
  print(index, x)

print('\n')
print("------------------------------------------------------------")

# Exercise 14: Pair Two Lists 
# Print "Alice: 85", "Ben: 73", etc. by pairing names with marks.
# Data:
# names = ["Alice", "Ben", "Carmen", "Dylan"]
# marks = [85, 73, 91, 66]

names = ["Alice", "Ben", "Carmen", "Dylan"]
marks = [85, 73, 91, 66]
for x in range(len(names)):
  print(f"{names[x]}, {marks[x]}")

print('\n')
print("------------------------------------------------------------")

# Exercise 15: Nested Loops – Times Table
# Print a 1–5 multiplication table with rows like:
# 1 2 3 4 5
# 2 4 6 8 10
# ...
# Use two for-loops (outer row 1..5, inner col 1..5).

for x in range(1,6):
  for y in range(1,6):
    print(x*y, end = " ")
  print()
  ## need to add a print() to go to next line

print('\n')
print("------------------------------------------------------------")

# Exercise 16: Pattern Printing (Right Triangle)
# For n = 5, print:
# *
# **
# ***
# ****
# *****
# Use a for-loop and string multiplication.
n = 5
for x in range(1,n+1):
  print("*" *x)

print('\n')
print("------------------------------------------------------------")

# Exercise 17: Dictionary Iteration (keys & values)
# Print "Alice : 72" etc. for each pair in the dict.
# Data:
# grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}

grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}
for name,score in grades.items(): 
  print(f"{name} : {score}")

print('\n')
print("------------------------------------------------------------")

# Exercise 18: Dictionary Aggregation
# Compute and print the average value in the dictionary (to 1 decimal place).
# Data:
# temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}
# Example: Output = 30.9

temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}

average = sum(temps.values()) / len(temps)

print(f"{average:.1f}")