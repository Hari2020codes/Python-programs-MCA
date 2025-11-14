class publisher:
    def getdetails(self):
        
            name=input("enter name of publisher")
            self.name=name
    def display(self):
        print("publisher: " ,self.name)        
        
    
class book(publisher):
    def getdetails(self):
        title=input("enter book details")
        author=input("enter name of author")
        self.title=title
        self.author=author
    def display(self):
        print("title: ",self.title)
        print("author: ", self.author)    

class python(book):
    price = 150
    pages = 400

    def pydetails(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Pages:", self.pages)

p1 = python()
p1.pydetails()
