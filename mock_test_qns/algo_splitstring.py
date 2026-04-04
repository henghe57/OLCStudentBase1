
##########################################
# Task 4
# Open a now Jupyterlab notebook and save the file as:
# TASK4_<your_name>_<your_class>_<index_number>.ipynb

# The task is to write a function remove_word(phrase) that removes
# consecutive repeated words in a phrase. The program:
# >> allows the user to input a phrase and convert to lower case [1]
# >> converts the phrase into a list of words. 
#     Do this without the help of the builtin
#     strings function such as str.split() [3]
# >> removes consecutive repeated words from the list [3]
# >> converts the list back into a new phrase. 
#      Do this without the help of the built-in
#     string functions such as str.join() [2]
# >> returns and displays the new phrase. [1]

# Save your Jupyterlab notebook for Task 4.

# Sample Output 1:
# Enter a phrase: Im a big big girl in a big big world
# New phrase: im a big girl in a big world

# Sample Output 2:
# Enter a phrase: Sorry sorry sorry sorry sorry naega naega
# New phrase: sorry naega

def remove_word(phrase):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # converts the phrase into a list of words.  [3] 

    # Code to split a string into a list without using .split()
    ### SIMPLE ENOUGH CODE - BUT DOES NOT CATCH SOME SCENARIOS
    wordlist = []
    thisword = ""
    for char in phrase:
        if char == " ":
            wordlist.append(thisword)
            thisword = ""
        else:
            thisword = thisword + char
    wordlist.append(thisword) # for the last word
    print(wordlist)
    
    #### COMPLEX CODE - BUT BETTER
    # separator = " "         # what separates one word from the next
    # position_separator = 0     # current position of delimiter
    # previous_position = 0         # position
    # wordlist = []              # list to hold the final output

    # while True: # while because you do not know how long this phrase is.
    #     # find the position of the " " separator from previous position
    #     position_separator = phrase.find(separator, previous_position)

    #     # if no separator found, means its the last word.
    #     if position_separator == -1:
    #         wordlist.append(phrase[previous_position:])
    #         break

    #     # slice the word from previous position, to the next separator
    #     wordpart = phrase[previous_position:position_separator]

    #     wordlist.append(wordpart) # append the sliced word

    #     # advance the previous position to next letter
    #     previous_position = position_separator + len(separator)
    
    # print(wordlist) # testing only

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # removes consecutive repeated words from the list [3]
    clean_wordlist = []

    for i in range(len(wordlist)):
        # handle first word, and add first word by default
        if i == 0:
            clean_wordlist.append(wordlist[i])
            continue
        
        # check if current word is the same as previous word
        if wordlist[i] != wordlist[i-1]:
            clean_wordlist.append(wordlist[i])
    
    # print(clean_wordlist) # testing only

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # converts the list back into a new phrase. [2]
    sentence = ""
    for w in clean_wordlist:
        sentence = sentence + w + " "

    # print(sentence) # testing only

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # returns and displays the new phrase. [1]
    return sentence


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # allows the user to input a phrase and convert to lower case [1]
phrase = input("Enter a phrase").lower()
# phrase = "Im Im a big big girl in a big big world".lower()
# phrase = "Sorry sorry sorry sorry sorry naega naega".lower()
cleaned = remove_word(phrase)
print(cleaned) # testing only



########################################################

# Scenario 4: Extracting Stock Prices for Market Analysis
# You are working for a stock exchange where hourly stock prices 
# for nVidia are recorded in a colon-separated string. 
# Your task is to extract all hourly stock prices 
# into a list of floats for further calculations.

# expected output
# [154.2, 158.7, 160.1, 163.4]

stockprice = "154.2:158.7:162.9:160.1:163.4:165.8:159.5:161.2:167.3:162.0:169.4:172.5:171.8:168.2:166.0:175.4:177.9:180.2:178.6:182.1:185.3:190.5:188.2:191.0:193.5:195.8:199.1:200.7:202.3:198.9"

# write your code here

lst = []
number = ""
for i in stockprice:
    if i == ":":
        lst.append(number)
        number = ""
    else:
        number += i
lst.append(number)
print(lst)
#-----------------------------------------
separator = " "
position_separator = 0
previous_position = 0
num_list = []
# while True: