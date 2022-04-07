# Реализация дека
class Deque:
    # Инициализация дека
    def __init__(self):
        self.deque = []
        self.size = 0

        # Количество элементов в деке
    def __len__(self):
        return self.size

    # Проверка дека на пустоту
    def is_empty(self):
        if len(self.deque) > 0:
            return False
        else:
            return True

    # Добавление нового элемента в начало дека
    def push(self, item):
        self.deque.append(item)

    # Добавление нового элемента в конец дека
    def push_left(self, item):
        self.deque.insert(0, item)

    # Извлечение элемента из начала дека
    def pop(self):
        # Проверка дека на пустоту
        self.is_empty()
        return self.deque.pop()

    # Извлечение элемента из конца дека
    def pop_left(self):
        # Проверка дека на пустоту
        self.is_empty()
        return self.deque.pop(0)

    # Нахождение элемента из начала дека
    def peek(self):
        if not self.is_empty():
            return self.deque[len(self.deque) - 1]

    # Нахождение элемента из конца дека
    def peek_left(self):
        if not self.is_empty():
            return self.deque[0]