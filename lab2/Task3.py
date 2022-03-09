chessBoard = [[0 for i in range(8)] for j in range(8)]
solutions = 0

# Поставим ферзя в клетку ij
def setQueen(i,j):
    for x in range(8):
        # Горизонталь
        chessBoard[x][j] += 1
        # Вертикаль
        chessBoard[i][x] += 1
        # Для заполнения диагоналей, сначала проверяем существует ли клетка с таким индексом
        if 0 <= i + j - x < 8:
            chessBoard[i + j - x][x] += 1
        if 0 <= i - j + x <8:
            chessBoard[i - j + x][x] += 1
    # -1 - обозначение ферзя в клетке
    chessBoard[i][j] = -1

def deleteQuenn(i,j):
    for x in range(8):
        # Освобождение горизонталь
        chessBoard[x][j] -= 1
        # Освобождение вертикаль
        chessBoard[i][x] -= 1
        # Освобождение диагонали
        if 0 <= i + j - x < 8:
            chessBoard[i+j-x][x] -= 1
        if 0 <= i - j + x <8:
            chessBoard[i - j + x][x] -= 1
    # Уберём ферзя
    chessBoard[i][j] = 0

# Функция для приятного глазу вывода
def outputAnswers():
    global solutions
    solutions += 1
    tempAlphabet = 'abcdefgh'
    answer = []
    for i in range(8):
        for j in range(8):
            if chessBoard[i][j] == -1:
                answer.append(tempAlphabet[j]+str(i+1))
    print('  '.join(answer))

# Рекурсивная функция, находит решения i-ой строки
def solveTask(i):
    # Ищем пустую клетку в строке
    for j in range(8):
        if chessBoard[i][j] == 0:
            # Если нашли ставим туда ферзя
            setQueen(i,j)
            # Если мы находимся в последней строке - выводим ответ, иначе поднимаемся на строку выше
            if i == 7:
                outputAnswers()
            else:
                solveTask(i + 1)
            deleteQuenn(i,j)

print("Решим задачу о 8 ферзях:"
      "\nНиже представлены все возможные решения")
solveTask(0)
print("Всего решений = " + str(solutions))