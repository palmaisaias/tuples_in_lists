#---Problem Statement:
#---You are maintaining a library system where each book is stored as a tuple within a list. 
#---Your task is to update this system by adding new books and ensuring no duplicates.

import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):  #adds book to library and also runs a check to block duplicates
    while True:
        print()
        print(Style.BRIGHT + '       Lets add a book!')
        book_title = input('What is the title of the book?: ').title().strip()
        print()
        author = input('Who is the author of the book?: ').title().strip()
        new_book = (book_title, author) #creates tuple with the input info
        if new_book in library: #if tuple is found in library list, will trigger message and break. 2 element tup check allows for mustiple book titles by same author
            print()
            print(f'    {Fore.LIGHTMAGENTA_EX + Style.BRIGHT + book_title + Style.RESET_ALL} by {Fore.LIGHTMAGENTA_EX + Style.BRIGHT + author + Style.RESET_ALL} is already in your library!')
            break
        library.append(new_book) #adds tup to library list
        print()
        print(f'    You have added {Fore.LIGHTCYAN_EX + Style.BRIGHT+ book_title + Style.RESET_ALL} by {Fore.LIGHTCYAN_EX + Style.BRIGHT + author + Style.RESET_ALL} to your library')
        break

def show_books(library):    #outputs current list of books 
    while True:
        print()
        print('Your current book collection:')
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        for b in library:   #calling by indexing. Prints a nicely formatted list
            print('⌈ ' + Style.BRIGHT + b[0] + Style.RESET_ALL)
            print('⌊ by: ' + b[1])
            print()
        break
    

def book_keeper(library):   #offers a simple menu with the option to add a book, view current library and quit the application
    while True:
        print()
        print('                       Digital Librarian')
        print('                       ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print('                             Menu')
        menu_inp = int(input('''
                1. Add a book to your library
                2. View your current book collection!
                3. Quit
                Enter menu option --> ''').strip())
        if menu_inp == 1:
            add_book(library)
        elif menu_inp == 2:
            show_books(library)
        elif menu_inp == 3:
            print()
            print(Fore.BLUE + Style.BRIGHT + "              Thanks for usind Digital Librarian!")
            print()
            break
        else:
            print()
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '                 Please enter a valid menu option')




book_keeper(library)