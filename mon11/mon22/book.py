class publisher:
    name = "abc"

class book(publisher):
    title = "py"
    author = "auth"

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
