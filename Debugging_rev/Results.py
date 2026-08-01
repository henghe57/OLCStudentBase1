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
count = 0 #10 start with 0 before entering student names

flag = True
while flag == True: #3 True to start loop 
    name = input("Enter student's name: ") #1 Replace the outer '' with "" to include the 's 
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #2 satisfy both conditions not just one
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] #4 out of the validation loop 
    count += 1
    if mark >= 75: #5 distinction includes 75
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] #6 [name] to be added into the list
    more = input('Would you like to enter another score, Y or N?: ') #8 N is not meant to be an integer
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) #7 sum() to take the overall divided by the quantity 
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") #9 string the variable count to be printed as string
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))
