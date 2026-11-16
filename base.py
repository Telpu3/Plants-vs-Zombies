class Base:
    def __init__(self, name, hp=500, max_units=10):
        self.name = name
        self.hp = hp
        self.max_units = max_units
        self.units = [] # Список юнитов, которых создала эта база

    def create_unit(self, unit, board):
        """Метод создания юнита на базе"""
        if len(self.units) >= self.max_units:
            print(f"[БАЗА {self.name}] Ошибка: Достигнут лимит юнитов ({self.max_units})!")
            return False
        
        # Проверяем, может ли поле вместить юнита
        if board.add_unit(unit):
            self.units.append(unit)
            print(f"[БАЗА {self.name}] Успешно создан юнит {unit.symbol}!")
            return True
        return False

    def on_unit_destroyed(self, unit):
        """Реакция на уничтожение юнита"""
        if unit in self.units:
            self.units.remove(unit)
            print(f"[БАЗА {self.name}] Юнит {unit.symbol} погиб. База учла потерю.")

    def show_status(self):
        """Отображение состояния базы"""
        print(f"\n--- СТАТУС БАЗЫ {self.name} ---")
        print(f"HP: {self.hp}")
        print(f"Юнитов: {len(self.units)} / {self.max_units}")