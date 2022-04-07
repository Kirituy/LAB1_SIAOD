from stack import Stack
from deque import Deque


def main():
    finish = False
    repeat = False
    while not finish:
        if not repeat:
            choose_task = input("=== Добро пожаловать в программу! === "
                                "\nВыберите и введите номер задания:"
                                "\nЗадание 1; "
                                "\nЗадание 2; "
                                "\nЗадание 3; "
                                "\nЗадание 4; "
                                "\nЗадание 5; "
                                "\nЗадание 6; "
                                "\nЗадание 7; "
                                "\nЗадание 8; "
                                "\nВаш ответ: ")
            repeat = True
        else:
            choose_task = input("=== Выберите и введите номер задания: ==="
                                "\nЗадание 1; "
                                "\nЗадание 2; "
                                "\nЗадание 3; "
                                "\nЗадание 4; "
                                "\nЗадание 5; "
                                "\nЗадание 6; "
                                "\nЗадание 7; "
                                "\nЗадание 8; "
                                "\nВаш ответ: ")
        # Задание 1
        if choose_task == "1":
            print("\n=== Задание 1: ===")

            with open('books.txt', encoding='utf-8') as file:
                lines = file.readlines()
                d1 = Deque()
                d2 = Deque()
                current = d1
                foreign = d2

                for i in range(len(lines)):
                    line = lines[i]
                    if current.is_empty():
                        current.push(line)
                    elif line <= current.peek_left():
                        current.push_left(line)
                    elif line >= current.peek():
                        current.push(line)
                    else:
                        while not current.is_empty():
                            e = current.pop_left()
                            if e < line:
                                foreign.push(e)
                            else:
                                foreign.push(line)
                                foreign.push(e)
                                while not current.is_empty():
                                    foreign.push(current.pop_left())
                                break
                        current, foreign = foreign, current

                while not current.is_empty():
                    print(current.pop_left())

        # Задание 2
        elif choose_task == "2":
            print("\n=== Задание 2: ===")

            with open('chifer.txt', encoding='utf-8') as file:
                decode_me = file.readlines()

                print("\nЗашифрованное сообщение: ")
                for line in decode_me:
                    print(line)

                message = Deque()
                decoded = Deque()
                for s in decode_me:
                    for c in s:
                        message.push(c)

                while not message.is_empty():
                    try:
                        c: str = message.pop_left()
                        if c.isalnum():
                            code = ord(c) - 1
                            decoded.push(chr(code))
                        elif c == " ":
                            decoded.push(c)

                    except e:
                        print(e)

                buffer = str()
                while not decoded.is_empty():
                    buffer += decoded.pop_left()

                print("\nРасшифрованное сообщение: ")
                print(buffer)

        # Задание 3
        elif choose_task == "3":
            print("\n=== Задание 3: ===")
            print("\nХанойская Башня ")

            def tower_of_hanoi(number_of_disks, start, auxiliary, end):
                if number_of_disks == 1:
                    print("Переместили диск 1 со стержня {} на стержень {}".format(start, end))
                    return
                tower_of_hanoi(number_of_disks - 1, start, end, auxiliary)
                print('Переместили диск {} со стержня {} на стержень {}'.format(number_of_disks, start, end))
                tower_of_hanoi(number_of_disks - 1, auxiliary, start, end)

            disks = int(input("\nВведите количество дисков: "))
            print("\nРешение задачи:")
            tower_of_hanoi(disks, 'A', 'B', 'C')

        # Задание 4
        elif choose_task == "4":
            print("\n=== Задание 4: ===")

            def check_brackets(string):
                brackets = Stack()
                for rb in string:
                    if rb == '(':
                        brackets.push(rb)
                    elif rb == ')':
                        if brackets.is_empty():
                            return False
                        brackets.pop()
                return brackets.is_empty()



            if check_brackets(input("\nВведите последовательность круглых скобок для проверки: ")):
                print("\nКоличество скобок слева совпадает с количеством скобок справа ")
            else:
                print("\nКоличество скобок слева НЕ совпадает с количеством скобок справа ")

        # Задание 5
        elif choose_task == "5":
            print("\n=== Задание 5: ===")

            def check_square_brackets(string):
                brackets = Deque()
                for sb in string:
                    if sb == '[':
                        brackets.push(sb)
                    elif sb == ']':
                        if brackets.is_empty():
                            return False
                        brackets.pop()
                return brackets.is_empty()

            if check_square_brackets(input("\nВведите последовательность квадратных скобок для проверки: ")):
                print("\nКоличество скобок слева совпадает с количеством скобок справа ")
            else:
                print("\nКоличество скобок слева НЕ совпадает с количеством скобок справа ")

        # Задание 6
        elif choose_task == "6":
            print("\n=== Задание 6: ===")

            with open('symbols.txt', encoding='utf-8') as file:
                text = str(file.readlines())
                print("\nИсходный текст файла: ")
                print(text)
                digits = Stack()
                letters = Stack()
                others = Stack()

                for c in text:
                    if c.isalpha():
                        letters.push(c)
                    elif c.isdigit():
                        digits.push(c)
                    else:
                        others.push(c)

                new_text = str()
                while not digits.is_empty():
                    new_text += str(digits.pop_left())

                new_text += " "

                while not letters.is_empty():
                    new_text += str(letters.pop_left())

                new_text += " "

                while not others.is_empty():
                    new_text += str(others.pop_left())

                print("\nОтсортированный текст файла: ")
                print(new_text)

        # Задание 7
        elif choose_task == "7":
            print("\n=== Задание 7: ===")

            with open('numbers.txt', encoding='utf-8') as file:
                strings = file.readlines()
                numbers = list()

                print("\nИсходный порядок чисел в файле: ")

                for line in strings:
                    numbers.append(int(line))

                for number in numbers:
                    print(number)

                print("\nИзменённый порядок чисел в файле: ")
                deque = Deque()

                for n in numbers:
                    if n < 0:
                        deque.push_left(n)
                    else:
                        deque.push(n)

                while not deque.is_empty():
                    x = deque.pop_left()
                    if x < 0:
                        deque.push(x)
                    else:
                        deque.push_left(x)
                        break

                while not deque.is_empty():
                    x = deque.pop()
                    if x < 0:
                        print(x)
                    else:
                        deque.push(x)
                        break

                while not deque.is_empty():
                    print(deque.pop_left())

        # Задание 8
        elif choose_task == "8":
            print("\n=== Задание 8: ===")

            with open('reverse_text.txt', encoding='utf-8') as file:
                words = file.readlines()
                stack = Stack()

                print("\nИсходный порядок слов в файле: ")

                for s in words:
                    s = s.strip()
                    print(s)
                    stack.push(s)

                print("\nИзменённый порядок слов в файле: ")

                while not stack.is_empty():
                    print(stack.pop())

        #  Возможность повтора выбора задания
        else:
            print("\nОтвет некорректен")

        wtr = input("\nВы желаете посмотреть другие задания? +/-? "
                    "\nВаш ответ: ")

        if wtr == "-":
            print("\n=== Сеанс завершён. Всего доброго! ===")
            finish = True
        elif wtr != "+":
            print("\nОтвет некорректен")


main()