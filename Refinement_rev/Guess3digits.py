import random
secret_code = ""
for i in range(3):
    digit = str(random.randint(1, 5))
    secret_code = secret_code + digit

print(secret_code)
print("Guess the 3-digit number. Each digit is from 1 to 5: ")
print("You have 5 tries. Enter your guess (e.g. 123). ")

for i in range(5):
    guess = input("Enter number: ")
    if guess == secret_code:
        print(f"Congrats! The answer is {secret_code}!")
        break
    else:
        count = 0
        for i in range(len(secret_code)):
            if secret_code[i] == guess[i]:
                count += 1 
        print(f"{count} digits are in the correct position.")    
if guess != secret_code:
    print(f"The answer is {secret_code}, better luck next time!")