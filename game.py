import copy

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Создаем сетку, заполненную точками 
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.units = [] # Хранение юнитов

    def add_unit(self, unit):
        # Ограничиваем максимальное количество юнитов
        if len(self.units) >= 20:
            print("Поле переполнено! Нельзя добавить больше 20 юнитов.")
            return False
        
        self.units.append(unit)
        # Ставим значок юнита на сетку 
        self.grid[unit.y][unit.x] = unit.symbol
        return True

    def remove_unit(self, unit):
        if unit in self.units:
            self.units.remove(unit)
            # Очищаем клетку
            self.grid[unit.y][unit.x] = '.'
            print(f"Юнит {unit.symbol} убран с поля.")

    def display(self):
        print("\n   " + " ".join(str(i) for i in range(self.width)))
        for y in range(self.height):
            row_str = " ".join(self.grid[y])
            print(f"{y:2} {row_str}")
        print()

    def copy_board(self):
        # Копирование поля вместе с юнитами 
        return copy.deepcopy(self)