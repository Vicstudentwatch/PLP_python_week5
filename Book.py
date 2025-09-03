class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    @property
    def get_author(self):
        return self.author
    
    def get_title(self):
        return self.title

class AnimeBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.genre = "Anime"
    

b1 = Book("Into the Ghetto","James")
ab1 = AnimeBook("Reincarneted as a Celeb","Unknown")

print(b1.get_author)
print(b1.get_title())
print(ab1.genre)


