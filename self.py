class Book:
    def setData(self):
        self.book_title = input('Enter Title - ')
        self.book_author = input('Enter author - ')
        self.book_category = input('Enter category - ')

    def getData(self):
        book_title = 'NA'
        book_author = 'NA'
        book_category = "NA"

        print(f'title  - {self.book_title}')
        print(f'author - {self.book_author}') 
        print(f'category - {self.book_category}')

b1 = Book()
b1.setData()
b1.getData()

b2 = Book()
b2.setData()
b2.getData()