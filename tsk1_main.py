class BooksItem:

    def __init__(self, authors_name: str, authors_surname: str, books_title: str, books_year: int, books_genre: str):
        self.authors_name = authors_name
        self.authors_surname = authors_surname
        self.books_title = books_title
        self.books_year = books_year
        self.books_genre = books_genre

    def print_info(self):
        print("== " * 7)
        print(f"author: {self.authors_name} {self.authors_surname}")
        print(f"title: {self.books_title}, year: {self.books_year}, genre: {self.books_genre}.")

    def __str__(self):
        result = f"{'-' * 10}\nauthor: {self.authors_name} {self.authors_surname}\ntitle: {self.books_title},\nyear: {self.books_year}, genre: {self.books_genre}."
        return result
    
first_book = BooksItem("first", "first", "first", 100, "first")
second_book = BooksItem("second", "sercond", "second", 110, "second")
third_book = BooksItem("third", "third", "third", 120, "third")
if __name__ == "__main__":
    third_book.print_info()
    print(str(second_book))
    print(first_book)
    print((repr(third_book)))

