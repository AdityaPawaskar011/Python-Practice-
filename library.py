class Book:

    def __init__(self,title,author,is_available):
        self.title= title
        self.author=author
        self.is_available=is_available
        self.quantity=0

obj= Book('a','a','Yes')
obj1= Book('b','b','Yes')    

# books=[]
class Library():
    
    book_dict=[]

    def add_book (self,book):
        Library.book_dict.append(
            {'title':book.title,'author':book.author,'is_available':book.is_available}
        )
        
        
    def borrow_book (self,title):
        for b in Library.book_dict:
            if b['title'] == title:
                if b['is_available'] == 'Yes':
                    ind = Library.book_dict.index(b)
                    # print(ind)
                    Library.book_dict.pop(ind)
                    




add=Library()
add.add_book(obj)
add.add_book(obj1)
add.borrow_book('a')
print(Library.book_dict)
