# This is a backup of original buggy code.
# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     else:
#         students = True

#AWARDS_DEBUGGING.py

students = True #10. If False, can never enter a loop
while students == True: 
    comp = int(input("Enter the Computing test score ")) #3. int() type
    math = int(input("Enter the Mathematics test score ")) #1. missing quotation mark
    joint_score = comp + math #4. math not comp again
    if comp >= 100 and math >= 100: #5. >= not >  
        print("Student is awarded a gold award")
    elif (comp >= 100 or math >= 100) and joint_score >= 180: #6. either one sub > 100 + #7. both must be more than 180 not or
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ").upper() #2. check for upper case
    if more_scores == 'N': #8. more_scores 
        students = False #9. If True, it will keep going no matter what
    else:
        students = True