# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:

    def __init__(self, rows, cols, value):  # rows - количество строк, cols - количество столбцов
      self.field = [[value for _ in range(cols)] for _ in range(rows)]
      self.rows = rows
      self.cols = cols
      self.value = value

#  принимаем новые значения:
    def get_val(self, row, col):
      return self.field[row][col]

#  заменяем существующие значения:
    def set_val(self, row, col, value):
      self.field[row][col] = value

#  возвращаем количество строк:
    def quantity_rows(self):
      return self.rows

#  возвращаем количество столбцов:
    def quantity_cols(self):
      return self.cols

matr = Matrix(7, 7, 0)
matr.set_val(5, 3, 1) #  заменили значение элемента 6-ой строки 4-го столбца с '0' на '1'
for r in range(matr.quantity_rows()):
    for c in range(matr.quantity_cols()):
        print(matr.get_val(r, c), end=' ')
    print()
print(f'Количество строк: {matr.quantity_rows()}\nКоличество столбцов: {matr.quantity_cols()}')