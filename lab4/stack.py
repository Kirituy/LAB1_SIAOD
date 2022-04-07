# Реализация стека
class Stack:
    # Инициализация стека
    def __init__(self):
        self.stack = []
        self.size = 0

    # Количество элементов в стеке
    def __len__(self):
        return self.size

    # Проверка стека на пустоту
    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    # Добавление нового элемента в начало стека
    def push(self, item):
        self.stack.append(item)

    # Добавление нового элемента в конец стека
    def push_left(self, item):
        self.stack.insert(0, item)

    # Извлечение элемента из начала стека
    def pop(self):
        # Проверка стека на пустоту
        self.is_empty()
        return self.stack.pop()

    # Извлечение элемента из конца стека
    def pop_left(self):
        # Проверка стека на пустоту
        self.is_empty()
        return self.stack.pop(0)

    # Нахождение элемента из начала стека
    def peek(self):
        if not self.is_empty:
            return self.stack[-1]

    # Нахождение элемента из конца стека
    def peek_left(self):
        if not self.is_empty:
            return self.stack[0]