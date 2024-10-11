class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def check_page(self):
        if self.pages <= 100:
            print(f'У вас {self.pages} страниц, толщина низкая')
        elif self.pages >= 100 <= 300:
            print(f'У вас {self.pages} страниц, толщина средняя')
        elif self.pages > 300:
            print(f'У вас {self.pages} страниц, толщина большая')

    def info(self):
        print(f'Книга {self.title}, Автор {self.author}, Страница {self.pages}')


book = Book('Baget', 'Baget', 235)
book.info()
book.check_page()


class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        return f' Название {self.name}, Цвет {self.color}, Размер {self.weight}'


new_fruit = Fruit('Яблоко', "Зелёный", '5-см')
print(new_fruit.info())