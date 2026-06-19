class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        name = input("نام کتاب: ")
        author = input("نویسنده: ")

        try:
            year = int(input("سال انتشار: "))
        except ValueError:
            print("سال انتشار باید عدد باشد.")
            return

        book = {
            "name": name,
            "author": author,
            "year": year
        }

        self.books.append(book)
        self.save_books()
        print("کتاب اضافه شد.")

    def show_books(self):
        if not self.books:
            print("هیچ کتابی وجود ندارد.")
            return

        for book in self.books:
            print(f"\nنام کتاب: {book['name']}")
            print(f"نویسنده: {book['author']}")
            print(f"سال انتشار: {book['year']}")
            print("-" * 20)

    def search_book(self):
        name = input("نام کتاب: ")

        for book in self.books:
            if book["name"].lower() == name.lower():
                print("\nکتاب پیدا شد.")
                print(f"نویسنده: {book['author']}")
                print(f"سال انتشار: {book['year']}")
                return

        print("کتاب پیدا نشد.")

    def delete_book(self):
        name = input("نام کتاب: ")

        for book in self.books:
            if book["name"].lower() == name.lower():
                self.books.remove(book)
                self.save_books()
                print("کتاب حذف شد.")
                return

        print("کتاب پیدا نشد.")

    def edit_book(self):
        name = input("نام کتاب مورد نظر: ")

        for book in self.books:
            if book["name"].lower() == name.lower():

                new_author = input(
                    f"نویسنده جدید ({book['author']}): "
                )

                try:
                    new_year = int(
                        input(
                            f"سال انتشار جدید ({book['year']}): "
                        )
                    )
                except ValueError:
                    print("سال انتشار باید عدد باشد.")
                    return

                if new_author:
                    book["author"] = new_author

                book["year"] = new_year

                self.save_books()
                print("کتاب ویرایش شد.")
                return

        print("کتاب پیدا نشد.")

    def save_books(self):
        with open("books.txt", "w", encoding="utf-8") as file:
            for book in self.books:
                file.write(
                    f"{book['name']},{book['author']},{book['year']}\n"
                )

    def load_books(self):
        try:
            with open("books.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if not line:
                        continue

                    name, author, year = line.split(",")

                    self.books.append({
                        "name": name,
                        "author": author,
                        "year": int(year)
                    })

        except FileNotFoundError:
            pass


library = Library()

while True:
    print("\n===== مدیریت کتابخانه =====")
    print("1- افزودن کتاب")
    print("2- نمایش کتاب‌ها")
    print("3- جستجوی کتاب")
    print("4- حذف کتاب")
    print("5- ویرایش کتاب")
    print("6- خروج")

    choice = input("انتخاب: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.delete_book()

    elif choice == "5":
        library.edit_book()

    elif choice == "6":
        library.save_books()
        print("اطلاعات ذخیره شد. خداحافظ!")
        break

    else:
        print("گزینه نامعتبر است.")