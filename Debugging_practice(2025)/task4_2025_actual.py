# This is a backup code. 

# group_1 = []
# group_2 = []
# group_3 = []
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_name = first_name[1]
#     age = input("Please enter the child's age: ")
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter >= "M" or age > 10:
#         group_2 = group_2 + [first_name]
#     elif age < 10:
#         group_3 = group_3 + [first_name]
#         count += 1
#     more = input("Do you have another child to enter, Y or N?: ")
#     if more == "Y":
#         flag = False

# print("You have entered the names of", flag, "children")
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)

group_1 = []
group_2 = []
group_3 = []
count = 0 #8. set the initial to 0
flag = True
while flag:
    first_name = input("Please enter the child's name: ").upper()
    first_letter = first_name[0] #1.variable shld be first_letter to store and #2. First index is 1
    age = int(input("Please enter the child's age: ")) #3. integer input
    if first_letter >= "A" and first_letter <= "M" and age > 10:
        group_1 = group_1 + [first_name]
    elif first_letter > "M" and age > 10: #5. 'and' not 'or' and #7.shld be > because of boundary
        group_2 = group_2 + [first_name]
    elif age <= 10: #6. '10 or lower'
        group_3 = group_3 + [first_name]
    count += 1 #9. always increment by 1 regardless of difference in ages and initials 
    more = input("Do you have another child to enter, Y or N?: ")
    if more != "Y": #4. if not it will keep looping
        flag = False

print("You have entered the names of", count, "children") #10. numbers not True or False children
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)