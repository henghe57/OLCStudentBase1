## This is a backup code.
# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))

name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #4: Should start from 0 not 1

flag = True
while flag == True: #1: True to start loop
    name = input("Enter student's name: ") #2: Double quotation mark not single
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #7: should be 'and' not 'or'
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] #9: should be de-dented
    count += 1
    if mark >= 75: #5: inclusive
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] #6: square bracket not bracket
    more = input('Would you like to enter another score, Y or N?: ') #3: no int() as it is a string input
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) #8: sum() not max() as it is using total not highest
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") #10: string the variable count
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))