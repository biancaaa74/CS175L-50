# bestseller_proj.py

def main():
    b = read_books()
    bestseller_file = open('bestsellers.txt','r')
    counter = 0
    for line in bestseller_file:
        counter += 1
    print("Read",counter,"Books")
    while(True):
        print('1: Look up year range')
        print('2: Look up month/year')
        print('3: Search for author')
        print('4: Search for title')
        print('Q: Quit')
        response = int(input('What would you like to do?: '))
        if response == 'Q':
            break
            print('Ending program')
        
        if response == 1:
            year_range(b)

        if response == 2:
            month_year(b)

        if response == 3:
            author(b)

        if response == 4:
            title(b)
    
    

def read_books():
    books_list = open('bestsellers.txt','r')
    booklist = []
    for book in books_list:
        cols = book.split('/t')
        booklist.append(cols)
    return booklist
    
def year_range(b):
    start_year = int(input('Please choose a start year: '))
    end_year = int(input('Please choose an end year: '))
    for book in b:
        date = book[3].split('/')
    if book[2] >= start_year or book[3] <= end_year:
        print(book)

def month_year(b):
    month = str(input('Please enter a month: '))
    year = str(input('Please enter a year: '))
    for book in b:
        date = book[3].split('/')
    if book[0] == month and book[2] == year:
        print(book)
    

def author(b):
    author = str(input("Please enter an author's name: "))
    for book in b:
        name = book[1]
    if author == name:
        print(book)

def title(b):
    book_title = str(input("Please enter the book's title: "))
    for book in b:
        title = book[0]
    if title == book_title:
        print(book)

main()
