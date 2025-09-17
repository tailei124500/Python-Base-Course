# 小型進階練習題：圖書管理系統(簡化版)
# 1. 建立Book類別
# 屬性:
#   --> title: 書名(字串)
#   --> author: 作者(字串)
#   --> year: 出版年份(整數)
# 方法:
#  --> __str__(): 回傳書籍的資訊
# 2.建立Library類別
# 屬性:
#   --> book_list:書籍清單(list of Book)
# 方法:
#   --> add_book(book): 新增一本書到圖書館
#   --> remove_book(title): 透過書名移除一本書，成功回傳True，找不到則回傳False
#   --> find_book(title): 透過書名查找一本書，找到回傳Book物件，否則回傳None
#   --> count_book_list(): 回傳館藏總數
# 3. 測試程式(main區域)
# 建立一個Library
# 建立3本Book物件，加入圖書館
# 測試:
#   --> 查詢某本書是否存在
#   --> 刪除某本書，並再次檢查館藏數量

import textwrap

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return textwrap.dedent(f"""\
        書名: {self.title}
        作者: {self.author}
        出版日期: {self.year}
        """)

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.book_list.append(new_book)

    def remove_book(self, title):
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)
                return True
        return False
    
    def find_book(self, title):
        for book in self.book_list:
            if book.title == title:
                return book
        return None
    
    def count_books(self):
        return len(self.book_list)
    
# test
# b1 = Book("哈利波特", "J.K.羅琳", 1997)
# b2 = Book("三國志", "陳壽", 280)
# b3 = Book("三體", "劉慈欣", 2006)

my_library = Library()

my_library.add_book("哈利波特", "J.K.羅琳", 1997)
my_library.add_book("三國志", "陳壽", 280)
my_library.add_book("三體", "劉慈欣", 2006)

print(f"館藏數量:{my_library.count_books()}")

print(my_library.find_book("三體"))

my_library.remove_book("三體")

print(f"館藏數量:{my_library.count_books()}")