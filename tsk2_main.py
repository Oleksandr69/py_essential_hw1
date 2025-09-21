class BooksReview:
    def __init__(self, name: str, review: str):
        self. name = name
        self.review = review

    def __str__(self):
        result = f"{self.name} написав відгук: {self.review}."
        return result
    
class BooksItem:

    def __init__(self, authors_name: str, authors_surname: str, books_title: str, books_year: int, books_genre: str):
        self.authors_name = authors_name
        self.authors_surname = authors_surname
        self.books_title = books_title
        self.books_year = books_year
        self.books_genre = books_genre
        self.books_response = []

    def add_review(self):
        name = input("Ваше ім'я: ")
        review = input("Ваш коментар: ")
        self.books_response.append(BooksReview(name=name, review=review))

    def print_info(self):
        print("== " * 10)
        print(f"author: {self.authors_name} {self.authors_surname}")
        print(f"title: {self.books_title}, year: {self.books_year}, genre: {self.books_genre}.")
        if self.books_response.__len__() == 0:
            print("-There are no reviews.-")
        else:
            for i, item in enumerate(self.books_response):
                print(f"{i+1}. {item.__str__()} - {item.__repr__()}")

    def __str__(self):
        reviews = ""
        if self.books_response.__len__() == 0:
            reviews = "-There are no reviews.-"
        else:
            for i, item in enumerate(self.books_response):
                reviews += f"\n{i + 1}. {item.__str__()}"
        info = f"{'---str---' * 5}\nauthor: {self.authors_name} {self.authors_surname}\ntitle: {self.books_title},\nyear: {self.books_year}, genre: {self.books_genre}."
        result = info + reviews
        return result
    
first_book = BooksItem("first", "first", "first", 100, "first")
second_book = BooksItem("second", "sercond", "second", 110, "second")
third_book = BooksItem("third", "third", "third", 120, "third")


third_book.add_review()
third_book.add_review()

third_book.print_info()
    # print(str(first_book))
print(third_book)
    # print((repr(third_book)))

