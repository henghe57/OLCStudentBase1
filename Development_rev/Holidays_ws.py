############################################################
# TASK 5 - HOLIDAY WORKSHOP BOOKING SYSTEM
############################################################

# A school is organising several holiday workshops.
# The school requires a program to create and store for workshop bookings.

# Open a new JupyterLab notebook and save it as:
# TASK5_.ipynb

# For each sub-task, add a comment using the hash symbol '#'
# at the beginning of your code to indicate the sub-task that the program code belongs to.

# For example:
# # Task 5.1
# Program Code

# All code should have appropriate comments and all identifiers should be appropriately named. [4]

# The following workshops and fees are available:
# ROB - Robotics - $48.00 per student
# WEB - Web Design - $36.00 per student
# PYT - Python Programming - $42.00 per student

# You can assume that a parent's name contains at least
# three characters.

############################################################
# Task 5.1 [4]
############################################################

# Write a function valid_workshop_code() that:

# - takes workshop_code as a parameter;
# - checks that the workshop code contains exactly three characters;
# - checks that the workshop code is ROB, WEB or PYT;
# - accepts the workshop code regardless of letter case;
# - returns True if the workshop code is valid or False  otherwise.
# - Display the appropriate reason for non valid workshop codes.

# Save your program.
# Task 5.1 
#______________________________________________________________

# workshop_code in ["ROB","WEB","PYT"]:
def valid_workshop_code(workshop_code):
    workshop_code = workshop_code.upper()
    if len(workshop_code) == 3:
        if workshop_code in ["ROB","WEB","PYT"]:
            return True
        else:
            print("Invalid code. Code must be either ROB, WEB or PYT.")
            return False
    else:
        print("Invalid code. Length of code must only contain 3 letters.")
        return False

# print(valid_workshop_code("ROB"))
# print(valid_workshop_code("henghyi"))



############################################################
# Task 5.2 [4]
############################################################

# Copy and paste your program from sub-task 5.1.

# Extend the program by writing a function
# calculate_booking_fee() that:

# - takes workshop_code (string) and number_of_students (integer) as parameters;
# - calculates the total fee using the appropriate fee per student;
# - deducts a discount of 10% if three or more students are included in the booking;
# - returns the total booking fee.

# You can assume that workshop_code and number_of_students are valid.

# Save your program.
# Task 5.2 
#______________________________________________________________

def calculate_booking_fee(workshop_code,number_of_students):
    number_of_students = int(number_of_students)
    workshop_code = workshop_code.upper()
    if workshop_code == "ROB":
        fee = 48.00
    elif workshop_code == "WEB":
        fee = 36.00
    elif workshop_code == "PYT":
        fee = 42.00
    total_fee = fee * number_of_students
    if number_of_students >= 3:
        total_fee *= 0.90
    
    return total_fee

# print(calculate_booking_fee("ROB",2))
# print(calculate_booking_fee("ROB",3))



############################################################
# Task 5.3 [2]
############################################################

# Copy and paste your program from sub-task 5.2.

# Extend the program by writing a function
# create_booking_reference() that:

# - takes parent_name and workshop_code as parameters;
# - generates a random six-digit booking number from 100000 to 999999 inclusive;
# - creates a booking reference containing:
#     - the first three characters of the parent's name in uppercase;
#     - the workshop code in uppercase;
#     - the six-digit booking number;
# - returns the booking reference.

# For example:
# Parent name: Siti
# Workshop code: pyt
# Random booking number: 583104
# Booking reference: SITPYT583104

# Save your program.
# Task 5.3
#______________________________________________________________

import random
def create_booking_reference(parent_name,workshop_code):
    booking_num = random.randint(100000,999999)
    booking_ref = (parent_name[:3].upper() + workshop_code.upper() + str(booking_num))
    return booking_ref

# print(create_booking_reference("heng","ROB"))



############################################################
# Task 5.4 [11]
############################################################

# Copy and paste your program from sub-task 5.3.

# The school requires an interface for the workshop booking system.

# the program must:
# Part 1: 
# - ask for the parent's name;
# - ask for a workshop code; call valid_workshop_code() to check the workshop code;
#       - keep asking until a valid workshop code is entered; store the valid workshop code in uppercase;
# - ask for the number of students;
#       - Validate that the input is a valid number
#       - keep asking until a whole number from 1 to 5 inclusive is entered;
# - call calculate_booking_fee() to calculate the booking fee;
# - call create_booking_reference() to create a booking reference;
# - display the booking reference and booking fee clearly.
# - Save the booking reference into a list called booking_list.
# - After each booking, ask the user to enter C to continue or Q to stop.

# Part 2:
# - save all the booking references in booking_list to the file workshop_bookings.txt, with one booking reference on each line;
# - store the total fee for all bookings to two decimal places at the end of the workshop_bookings.txt file.
#   e.g. "Total Fee : $192.86"

# Suitable input and output messages must be used.
# Save your JupyterLab notebook for Task 5.

# Task 5.4 
#______________________________________________________________

booking_list = []
total_fee = 0
while True:
    parent_name = input("Enter parent's name: ")
    while True:
        workshop_code = input("Enter workshop code: ")
        if valid_workshop_code(workshop_code) == False:
            print("Invalid workshop code.")
        else:
            workshop_code = workshop_code.upper()
            break
    while True:
        num = input("Enter the number of students (1-5): ")
        if not num.isdigit():
            print("You must enter a number")
        else:
            if 1 <= int(num) <= 5:
                num_of_students = int(num)
                break
            else:
                print("Invalid. Number must be between 1 to 5.")
    booking_fee = calculate_booking_fee(workshop_code,num_of_students)
    booking_reference = create_booking_reference(parent_name,workshop_code)

    print(f"Booking reference: {booking_reference}")
    print(f"Booking fee: ${booking_fee:.2f}")

    booking_list.append(booking_reference)
    total_fee += booking_fee
    
    choice = input("Do you want to continue booking? Press C to continue, else Q to quit: ").upper()
    if choice == "Q":
        break

with open("workshop_bookings.txt","w") as file:
    for booking in booking_list:
        file.write(booking + "\n")
    file.write(f"Total fee: {total_fee:.2f}")



        


