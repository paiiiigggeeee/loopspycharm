number_of_books = int(input('How many books to buy?'))

total = 0

for book in range(number_of_books):
    book_price = float(input('Enter book price in $'))
    if book_price == 0:
        print ('Yay! Free book!')
    total = total + book_price

print('The total price for all books is $ ' + str(total))
