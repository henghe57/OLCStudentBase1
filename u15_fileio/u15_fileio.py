# 3 modes, r, w, a

# write mode
# if file does not exist, it will create it.
# if file exists, it will overwrite it.

# create a file 
# file = open('filename.txt','a')
# to write to a file 
# file.write('Next year will be the best.')
# close the file
# file.close()
# with open('filename.txt','r') as file:
#     content = file.read()
#     print(content)

# counter = 0
# for x in content:
#     if x.lower() == "a":
#         counter += 1
# print(f"There are {counter} a's in the file.")

# choose a random day of the week
# import random
# with open("filename.txt", "r") as content:
#     daylist = content.readlines()
#     for day in daylist:
#         print(day)#, end="")

# random_day = random.choice(daylist)
# print(f"Random day: {random_day}")


# planets_list = ["mercury\n","earth\n","venus\n","mars\n","jupiter\n","saturn\n","uranus\n","sun\n"]
# with open("planets.txt","w") as content:
#     content.writelines(planets_list)

# task_list = ["Badminton training\n","Computing AA\n","Math revisions\n"]
# while True:
#     task = input("What is your objective today?: ")
#     proceed = input("Type N to stop: ").upper()
#     if proceed == "N":
#         with open("tasks.txt","a") as content:
#             content.writelines(task_list)
#         break

print("-----------------------------------------")

# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_stored. 

data_stored = {} # empty dictionary
shapes_list = ["star\n","sphere\n","square\n","triangle\n"]
with open("shapes.txt","w") as content1:
    content1.writelines(shapes_list)
colours_list = ["red\n","yellow\n","green\n","blue\n"]
with open("colours.txt","w") as content2:
    content2.writelines(colours_list)