class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name} by {self.author}, {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}, chief editor: {self.chief_editor}")




if __name__ == '__main__':
    book = Book("The Impossible Fortune", "Richard Osman", 224)
    magazine = Magazine("National Geographic", "Shekar Gupta")

    book.print_information()
    magazine.print_information()