ID = ""
counter = 0
numEntries = input("How many entries? ")
for i in range(int(numEntries)):
    while True:
        ID = input("Enter ID: ")
        if len(ID) != 9:
            print("Error. Length of ID must be 9.")
        else:
            break
    if ID[0] == "S" or ID[0] == "T":
        counter += 1 
        print("Welcome home!")
    else:
        print("Welcome to Singapore!")
print(f"Total number of Singaporeans: {counter}")
