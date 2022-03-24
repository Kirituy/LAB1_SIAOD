# Программа поиска подстроки в строке через выбранный пользователем алгоритм
import time
from timeit import default_timer as timer

# Ввод пользователем строки
string = input("Введите строку - ")
# Ввод пользователем подстроки
sub_string = input("Введите подстроку, которую необходимо найти - ")

start_task = True

while start_task:

    # Изменение строки
    change_s = input("\nВы хотите изменить строку? +/- Ваш ответ: ")
    if change_s == "+":
        # Ввод пользователем строки
        string = input("Введите строку - ")
        # Ввод пользователем подстроки
        sub_string = input("Введите подстроку, которую необходимо найти - ")

    elif change_s == "-":
        # Изменение подстроки
        change_sub = input("\nВы хотите изменить подстроку? +/- Ваш ответ: ")
        if change_sub == "+":
            # Ввод пользователем подстроки
            sub_string = input("Введите подстроку, которую необходимо найти - ")
        elif change_sub != "-":
            print("\nВведён некорректный символ. Ответ по умолчанию: '-'")

    elif change_s != "-":
        print("\nВведён некорректный символ. Ответ по умолчанию: '-'")

    # Возможность отключения чувствительности к регистру
    sen = True
    sensitivity = input("\nВы хотите отключить чувствительность к регистру при поиске? +/- Ваш ответ: ")
    if sensitivity == "+":
        sen = False
    elif sensitivity != "-":
        print("\nВведён некорректный символ. Ответ по умолчанию: '-'")

    # Выбор алгоритма поиска
    choose_algorithm = input("\nВыберите алгоритм поиска, введя его номер"
                             "\n1. Алгоритм Кнута-Морриса-Пратта;"
                             "\n2. Упрощенный алгоритм Бойера-Мура;"
                             "\n3. Стандартная функция поиска."
                             "\nВаш ответ: ")

    if choose_algorithm == "1":
        # Алгоритм префикс-функции
        def prefix(s: str) -> list:
            p = [0] * len(s)
            i = 0
            j = 1

            while j < len(s):
                if s[i] == s[j]:
                    p[j] = i + 1
                    i += 1
                    j += 1
                elif i:
                    i = p[i - 1]
                else:
                    p[j] = 0
                    j += 1
            return p

        # Алгоритм Кнута-Морриса-Пратта
        def kmp(s: str, sub: str) -> str:
            print("\nДлина строки: " + str(len(s)), "\nДлина подстроки: " + str(len(sub)))
            if not len(s) or len(sub) > len(s):
                return str([])

            p = prefix(sub)
            i = j = 0

            while i < len(s):
                if sub[j] == s[i]:
                    i += 1
                    j += 1

                    if j == len(sub):
                        return "\nРасположение найденной в строке подстроки: " + str(i - len(sub))

                elif j > 0:
                    j = p[j - 1]
                else:
                    i += 1

            return "\nВведённая подстрока не найдена"


        # Вызов функции поиска
        if not sen:
            start = timer()
            print(kmp(string.lower(), sub_string.lower()))
            end = timer()
            print("Time taken:", end - start, " секунд")
        else:
            start = timer()
            print(kmp(string, sub_string))
            end = timer()
            print("Time taken:", end - start, " секунд")

    elif choose_algorithm == "2":
        # Функция предкомпиляции строки
        def bm_pred_compil(sub: str) -> list:
            d = [len(sub) for _ in range(1105)]
            for i in range(len(sub)):
                d[ord(sub[i])] = len(sub) - i
            return d

        # Алгоритм Бойера-Мура
        def bm(s: str, sub: str) -> str:
            print("\nДлина строки: " + str(len(s)), "\nДлина подстроки: " + str(len(sub)))

            d = bm_pred_compil(sub)
            i = j = k = len(sub)

            while j > 0 and i <= len(s):
                if s[k - 1] == sub[j - 1]:
                    k -= 1
                    j -= 1

                else:
                    i += d[ord(s[k - 1])]
                    j = len(sub)
                    k = i

            if j <= 0:
                return "\nРасположение найденной в строке подстроки: " + str(k)
            else:
                return "\nВведённая подстрока не найдена"


        # Вызов функции поиска
        if not sen:
            start = timer()
            print(bm(string.lower(), sub_string.lower()))
            end = timer()
            print("Time taken:", end - start, " секунд")
        else:
            start = timer()
            print(bm(string, sub_string))
            end = timer()
            print("Time taken:", end - start, " секунд")

    elif choose_algorithm == "3":
        # Стандартная функция поиска
        def standart_search(s: str, sub: str) -> str:
            k = -1
            for i in range(len(s) - len(sub) + 1):
                success = True
                for j in range(len(sub)):
                    if sub[j] != s[i + j]:
                        success = False
                        break

                if success:
                    k = i
                    break

            if k != -1:
                return "\nРасположение найденной в строке подстроки: " + str(k)
            else:
                return "\nВведённая подстрока не найдена"


        # Вызов функции поиска
        if not sen:
            start = timer()
            print(standart_search(string.lower(), sub_string.lower()))
            end = timer()
            print("Time taken:", end - start, " секунд")
        else:
            start = timer()
            print(standart_search(string, sub_string))
            end = timer()
            print("Time taken:", end - start, " секунд")

    else:
        print("Введён некорректный номер алгоритма")

    # Пользователь выбирает, хочет ли он повторить процедуру поиска
    start_stop = input("\nВы хотите повторить процедуру поиска, использовав другой алгоритм? +/- Ваш ответ: ")
    if start_stop == "-":
        start_task = False
    elif start_stop != "+":
        print("\nВведён некорректный символ. Ответ по умолчанию: '+'")