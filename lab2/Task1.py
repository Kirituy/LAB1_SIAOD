import random
import Node
from timeit import default_timer as timer


def BinarySearch(mas, target):
    first = 0
    last = len(mas) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = first + last
        mid = mid // 2
        if mas[mid] == target:
            index = mid
        else:
            if target < mas[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

def fibonacci_search(lst, target):
    size = len(lst)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None

def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

rangeee=int(input("\nВведите длину массива = "))
mas = [random.randint(-1000, 1000) for i in range(rangeee)]
print("Массив: ", mas)

answerAdd = input('\nХотите ли вы добавить элемент в исходный массив? Введите "да" или "нет". Ваш ответ: ')
if answerAdd == "да":
    U = [int(input("\nВведите индекс элемента, который хотите добавить = "))]
    mas.extend

answerDel = input('\nХотите ли вы удалить элемент из исходного массив? Введите "да" или "нет". Ваш ответ: ')
if answerDel == "да":
    Y = int(input("\nВведите индекс элемента, который необходимо удалить = "))
    mas.remove(Y)

mas.sort()
print("Отсортированный Массив: ", mas)

val = int(input("\nНайти число X: "))

start = timer()
print("\nБИНАРНЫЙ ПОИСК:")
print("Число", val, "находится в индексе", BinarySearch(mas, val))
end = timer()
print("Time taken:", end-start)

start = timer()
print("\nФибоначчи ПОИСК:")
print("Число", val, "находится в индексе", fibonacci_search(mas, val))
end = timer()
print("Time taken:", end-start)

start = timer()
print("\nИТНЕРПОЛЯЦИОННЫЙ ПОИСК:")
print("Число", val, "находится в индексе", InterpolationSearch(mas, val))
end = timer()
print("Time taken:", end-start)

# Воспользуемся поиском через бинарное дерево
# Преобразование массива в бинарное дерево
root = None
for i in range(len(mas)):
    root = Node.insert(root, mas[i], i)

print("\nПоиск через бинарное дерево: ")

# Функция поиска элемента в бинарном дереве
def treeSearch(root, value):
    if root is None:
        raise ValueError()

    if value > root.data:
        return treeSearch(root.right, value)
    elif value < root.data:
        return treeSearch(root.left, value)
    else:
        print("Число", value, "находится в индексе ", root.index)


# Вызов функции поиска в бинарном дереве
start = timer()
treeSearch(root, val)
end = timer()
print("Time taken:", end-start)

