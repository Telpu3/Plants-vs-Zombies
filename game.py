import copy
import random
from landscape import Grass, Water, Roof
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.units = [] # Хранение юнитов
        self.grid = []
        # Сначала заполняем всё травой
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Grass().symbol) # '.'
            self.grid.append(row)
        # 2. Расставляем пятна воды 
        for _ in range(3):
            cx = random.randint(2, width - 3)
            cy = random.randint(0, height - 3)
            for dy in range(3):
                for dx in range(3):
                    self.grid[cy + dy][cx + dx] = Water().symbol # '~'
        # 3. Строим пятна крыш 
        for _ in range(2):
            cx = random.randint(2, width - 2)
            cy = random.randint(0, height - 2)
            for dy in range(2):
                for dx in range(2):
                    self.grid[cy + dy][cx + dx] = Roof().symbol # '^'
            
    def add_unit(self, unit):
        # Ограничиваем максимальное количество юнитов
        if len(self.units) >= 20:
            print("Поле переполнено! Нельзя добавить больше 20 юнитов.")
            return False
        # 1. Проверяем, не занята ли клетка
        if self.grid[unit.y][unit.x] not in ['.', '~', '^']:
            print(f"Клетка ({unit.x}, {unit.y}) уже занята! Выберите другую.")
            return False

        # 2. Проверяем ландшафт
        cell_type = self.grid[unit.y][unit.x]
        is_zombie = "Zombie" in unit.__class__.__name__
        
        # Зомби не могут ходить по крышам
        if cell_type == '^' and is_zombie:
            print("Зомби не может забраться на крышу!")
            return False
            
        # Растения не могут расти в воде 
        if cell_type == '~' and not is_zombie:
            print("Растение не может расти в воде!")
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