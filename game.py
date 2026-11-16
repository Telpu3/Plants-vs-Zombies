import copy
import random
from landscape import Grass, Water, Roof
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.units = [] # Хранение юнитов
        self.grid = []
        # Генерируем случайный ландшафт (3 типа)
        for y in range(height):
            row = []
            for x in range(width):
                if x < width // 3:
                    row.append(Grass().symbol)  # Левая треть - трава
                elif x < (width // 3) * 2:
                    row.append(Water().symbol)  # Средняя треть - вода
                else:
                    row.append(Roof().symbol)   # Правая треть - крыша
            self.grid.append(row)
            
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
    def get_unit_at(self, x, y):
        for unit in self.units:
            if unit.x == x and unit.y == y:
                return unit
        return None
    def display(self):
        print("\n   " + " ".join(str(i) for i in range(self.width)))
        for y in range(self.height):
            row_str = " ".join(self.grid[y])
            print(f"{y:2} {row_str}")
        print()

    def copy_board(self):
        # Копирование поля вместе с юнитами 
        return copy.deepcopy(self)