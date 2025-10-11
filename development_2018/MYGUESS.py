## Question 10, 12

while True: 
    p1 = int(input("Enter a whole num between 1 to 50: "))
    if p1 < 0 or p1 > 50:
        print("Invalid num, must be between 1 to 50.")
    else: 
        break

# guesses = 5
# for i in range(guesses):
#     p2 = int(input(f"Guess p1 number, you have {guesses} guesses: "))
#     if p2 == p1:
#         print("Congrats. You have guessed the correct number.")
#         break
#     elif p2 != p1:
#         guesses -= 1
#         print("Your guess is incorrect. Try again.")
#         if p2 > p1:
#             print("Your guess is higher than the number.")
#         else:
#             print("Your guess is lower than the number.")
# if guesses == 0:
#     print("Game over!")
#     print(f"The number was {p1}.")

print("--------------------------------------------------------")

## Question 13

guesses = 0
mode = input("Choose a difficulty: ")
if mode == "Easy":
    guesses = 8
elif mode == "Intermediate":
    guesses = 6
elif mode == "Hard":
    guesses = 4
else: 
    print("Invalid difficulty.")

for i in range(guesses):
    p2 = int(input(f"Guess p1 number, you have {guesses} guesses: "))
    if p2 == p1:
        print("Congrats. You have guessed the correct number.")
        break
    elif p2 != p1:
        guesses -= 1
        print("Your guess is incorrect. Try again.")
        if p2 > p1:
            print("Your guess is higher than the number.")
        else:
            print("Your guess is lower than the number.")
if guesses == 0:
    print("Game over!")
    print(f"The number was {p1}.")