# Создадим класс хэш-таблицы
class HashTable:
    size = int(input("Введите размер хэш-таблицы: "))
    size = size+1
    def __init__(self):
        self.data = [None] * self.size

    # Получение содержимого баккета
    def __getitem__(self, key):
        h = self.getHash(key)
        try:
            while self.data[h]:
                if self.data[h] and self.data[h].get(key):
                    return self.data[h]
                h = self.getRehash(h)
        except IndexError:
            return

    # Заполнение пустого баккета
    def __setitem__(self, key, value):
        h = self.getHash(key)
        if self.data[h] is None:
            self.data[h] = {key: value}
            return

        next_h = self.getRehash(h)
        try:
            while self.data[next_h] is not None:
                if self.data[next_h].get(key):
                    self.data[next_h].get(key)
                    break
                next_h = self.getRehash(next_h)
        except IndexError:
            raise
        self.data[next_h] = {key: value}

    # Хэш-функция
    def getHash(self, name):
        return len(name) % self.size

    # Функция рехэширования
    def getRehash(self, oldhash):
        return oldhash + 1


# Заполним хэш-таблицу двумя значениями
table = HashTable()
for i in range(table.size-1):
    table[input('\nВведите ключ ')] = input('\nВведите значение ')
#table[input('\nВведите ключ ')] = input('\nВведите значение ')

answer = input ('Вы хотите найти значение по ключу? Введите "да" или "нет". Ваш ответ:  ')
if answer == 'да':
    # Выводим одно из значений через ключ
    print(table[input('\nВыберите значение по ключу ')])
