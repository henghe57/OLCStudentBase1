# caesar encryption 

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter = "J"
key = 3
index = letters.find(letter)

print(index)

newindex = index + 3
encrypted_char = letters[newindex]

print(encrypted_char)

print("----------------------------------------")

# word = input("Enter an alphabet: ")
# shift = int(input("Shift by: "))
# print(chr(65 + ((ord(word)-65 + shift)%26)))

print("----------------------------------------")

# ori = input("Enter your text: ")
# shift = int(input("Shift by: "))
# ans = ""
# for x in ori:
#     print(x)
#   current = ord(x)
#   ans = ans + chr(current + shift)
# print(ans.upper())