book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

# book = input('Please enter the title of a book: ')
# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")

#----------------------------------------------------------------------
# Task 3.1

# book = input('Please enter the title of a book: ')
# book = book[0].upper() + book[1:]

#----------------------------------------------------------------------
# Task 3.2

# book = input('Please enter the title of a book: ')
# book = book[0].upper() + book[1:]
# author = input(f"Please enter the author of the book {book}: ")
# author = author[0].upper() + author[1:]
# print(f"The author of this book named {book} is written by {author}.")

#----------------------------------------------------------------------
# Task 3.3
# add = input("Would you like to add a book> Y or N: ")
# if add == "Y":
#     book = input('Please enter the title of a book: ')
#     book = book[0].upper() + book[1:]
#     author = input(f"Please enter the author of the book {book}: ")
#     author = author[0].upper() + author[1:]
#     print(f"The author of this book named {book} is written by {author}.")
#     book_authors[book] = author
#     print(book_authors)

#----------------------------------------------------------------------
# Task 3.4
add = input("Would you like to add a book> Y or N: ")
if add == "Y":
    book = input('Please enter the title of a book: ')
    book = book[0].upper() + book[1:]
    author = input(f"Please enter the author of the book {book}: ")
    author = author[0].upper() + author[1:]
    print(f"The author of this book named {book} is written by {author}.")
    book_authors[book] = author
    print(book_authors)

amend = input("Would you like to change the author of a book? Y or N: ")
if amend == "Y":
    book = input(f"Please enter the title of a book: ")

    while True:
        new_author = input(f"Enter a new author to replace the current author of the {book}: ")
        gotnum = False
        for i in new_author:
            if i.isdigit():
                gotnum = True
                break

        if gotnum == True:
            print("Author cannot contain numbers. Please try again.")
        else:
            book_authors[book[0].upper() + book[1:]] = new_author[0].upper() + new_author[1:]
            break
print(book_authors)