grades = {
    "Алиса": 100,
    "Боб": 60,
    "Анна": 49,
    "Максим": 50,
    "Катя": 3,
    "Дмитрий": 99,
    "Света": 0,
    "Елена": 29,
    "Никита": 52,
    "Оля": 87
}

max_ball = grades.values()
max_balls = max(max_ball), min(max_ball)
print(max_balls)


def total_product(product):
    product = {
        "яблоки": 5,
        "бананы": 2,
        "молоко": 0,
        "хлеб": 3,
        "яйца": 12,
        "сыр": 0,
        "курица": 2
    }
    maximum = product.values()
    sammer = sum(maximum)
    print(sammer)


total_product('готово')
product = {
    "яблоки": 5,
    "бананы": 2,
    "молоко": 0,
    "хлеб": 3,
    "яйца": 12,
    "сыр": 0,
    "курица": 2,
}


def no_product(product):
    out = []
    for product, coun in product.items():
        if coun == 0:
            out.append(product)

    return f"Столько прдуктов не хватает: {out}"


print(no_product(product=product))

grades = {
    "Алиса": 100,
    "Боб": 60,
    "Анна": 49,
    "Максим": 50,
    "Катя": 3,
    "Дмитрий": 99,
    "Света": 0,
    "Елена": 29,
    "Никита": 52,
    "Оля": 87
}


def count_mark(grades, target_score):
    result = []
    for name, score in grades.items():
        if score == target_score:
            result.append(name)
    if result:
        print(f"Ученики с оценкой {target_score}: {(result)}")
    else:
        print(f"Нет учеников с оценкой {target_score}")


count_mark(grades, target_score=int(input("Введите число: ")))


def marker(one):
    for one in range(1, 50):
        print(one)


marker(one=int(input('Введите число')))