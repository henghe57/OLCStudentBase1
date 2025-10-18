# Paper 2 - 2025 O Level Computing
# Question for Task 2
word_list = ["apple", "window", "bend", "paper", "thought"]

# Task 2.1 [3]

# Extend the program to:
# - ask the user to input a new word
# - take the new word as input
# - convert the new word to lower case
# - store the new word at the end of the list in a new space

# You do not need to consider any validation for the new word.

# Save your program

# ----------------------------------------------

new = input("Enter a new word: ").lower()
word_list.append(new)
print(word_list)

# ----------------------------------------------
# Task 2.2 [4]

# Copy and paste your program from sub-task 2.1

# Extend your program to 
# - search the list to find words that have 5 or more letters
# - count and output the number of words that have five or more letters, with a suitable output message.

# Save your program 
# ----------------------------------------------
counter = 0
for word in word_list:
    if len(word) >= 5:
        counter += 1
print(counter)
print(f"The number of words that have 5 or more letters in the list is {counter}.")

# ----------------------------------------------
# Task 2.3 [3]

# Copy and paste your program from sub-task 2.2

# Extend your program to :
# - search the list to find words that begin and end with the same letter
# - count and output the number of words that begin and end with the same letter, with a suitable output message.

# Save your program for Task 2
# ----------------------------------------------

counter = 0 
for word in word_list:
    if word[0] == word[-1]:
        counter += 1
print(counter)
print(f"The number of words that begin and end with the same letter is {counter}.")