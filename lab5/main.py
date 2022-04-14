from math import*
from turtle import*
import time

# Функция рисующая фрактал дерева Пифагора
def fractal(aturt, depth, maxdepth):
   if depth > maxdepth:
     return
   length = 180*((sqrt(2)/2)**depth)
   anotherturt = aturt.clone()
   aturt.forward(length)
   aturt.left(45)
   fractal(aturt, depth+1, maxdepth)
   anotherturt.right(90)
   anotherturt.forward(length)
   anotherturt.left(90)
   anotherturt.forward(length)
   if depth != maxdepth:
     turt3 = anotherturt.clone()
     turt3.left(45)
     turt3.forward(180*((sqrt(2)/2)**(1+depth)))
     turt3.right(90)
     fractal(turt3, depth+1, maxdepth)
   anotherturt.left(90)
   anotherturt.forward(length)


# Основная функция
def main():
    print("=== Добро пожаловать в программу реализации фрактала 'Дерево Пифагора'! ===")

    # Количество вызовов рекурсии. Задание глубины фрактала.
    deep: int = 0
    try:
        deep = int(input("\nВведите значение глубины фрактала: "))

    except ValueError:
        print("\nОтвет некорректен. Нужно вводить число")

    start_time = time.time()
    window = Screen()
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-75, -225)
    t.pendown()
    t.speed(1000)
    t.left(90)

    # Вызов функции треугольника Серпинского
    fractal(t, 0, deep)

    print("\nОтрисовка фрактала полностью завершена")
    print(f"\nВремя выполнения составило: {time.time() - start_time} секунд")

    print("\n=== Сеанс завершён. Всего доброго! ===")
    window.exitonclick()

main()