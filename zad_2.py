class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street} ({self.zip_code}), Open hours: {self.open_hours}"


library1 = Library(city="Warsaw", street="Jana Pawła", zip_code="00-001",
                   open_hours="9:00 - 16:00 ", phone="123-456-789")
library2 = Library(city="Katowice", street="Mariacka", zip_code="40-200",
                   open_hours="10:00 - 17:00", phone="987-654-321")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return f"{self.first_name} {self.last_name}, hired on {self.hire_date}"


employee1 = Employee(first_name="Jarek", last_name="Sztos", hire_date="2022-01-15",
                     birth_date="1990-05-20", city="Katowice", street="Mariacka")
employee2 = Employee(first_name="Alicja", last_name="Kowalska", hire_date="2023-03-10",
                     birth_date="1995-08-12", city="Warsaw", street="Jana Pawła")
employee3 = Employee(first_name="Janek", last_name="Jan", hire_date="2013-11-03",
                     birth_date="1985-11-23", city="Warsaw", street="Jana Pawła")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book by {self.author_name} {self.author_surname}, published on {self.publication_date}"


book1 = Book(library=library1, publication_date="2023-03-01",
             author_name="Andrsej", author_surname="Sapkowski", number_of_pages=700)
book2 = Book(library=library2, publication_date="1902-12-15",
             author_name="Mark", author_surname="Twain", number_of_pages=250)
book3 = Book(library=library1, publication_date="2016-02-19",
             author_name="George", author_surname="Martin", number_of_pages=1200)
book4 = Book(library=library2, publication_date="1897-07-09",
             author_name="Frank", author_surname="Kafka", number_of_pages=180)
book2 = Book(library=library2, publication_date="2012-07-24",
             author_name="Robert", author_surname="Stonka", number_of_pages=50)


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}"


student1 = Student(first_name="Anna", last_name="Stara")
student2 = Student(first_name="Jan", last_name="Chlebowski")
student3 = Student(first_name="Marek", last_name="Miarka")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_titles = ", ".join([book.author_surname for book in self.books])
        return f"Order by {self.student} ({self.order_date}): {book_titles}"


order1 = Order(employee=employee1, student=student1, books=[book2], order_date="2024-02-10")
order2 = Order(employee=employee2, student=student3, books=[book1, book3], order_date="2024-03-20")


print(order1)
print(order2)

