from abc import ABC, abstractmethod

# 1. классы ландшафта

class Landscape(ABC):
    """Базовый интерфейс для всех типов ландшафта"""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def get_effect(self):
        """Метод, описывающий влияние ландшафта на юнита"""
        pass

class Grass(Landscape):
    def __init__(self):
        super().__init__("Грядка", ".")
    def get_effect(self):
        return "Обычная клетка. Никаких штрафов."

class Water(Landscape):
    def __init__(self):
        super().__init__("Бассейн", "~")
    def get_effect(self):
        return "В воде зомби замедляются (если у них нет жилета)."

class Roof(Landscape):
    def __init__(self):
        super().__init__("Крыша", "^")
    def get_effect(self):
        return "С крыши нельзя стрелять по прямой."

# 2. Нейтральные обьекты
class NeutralObject(ABC):
    """Базовый интерфейс для всех нейтральных объектов"""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def interact(self, unit):
        pass

class Sun(NeutralObject):
    def __init__(self):
        super().__init__("Солнце", "☀️")
    def interact(self, unit):
        pass 

class Lawnmower(NeutralObject):
    def __init__(self):
        super().__init__("Газонокосилка", "🚜")
    def interact(self, unit):
        pass

class Grave(NeutralObject):
    def __init__(self):
        super().__init__("Могила", "🪦")
    def interact(self, unit):
        pass

class Wheelbarrow(NeutralObject):
    def __init__(self):
        super().__init__("Тачка", "🛒")
    def interact(self, unit):
        pass

# 3. Перегрузка
def mixin_interaction(unit_class):
    """Функция-декоратор для добавления перегрузки в класс Unit"""
    def __add__(self, other):
        if isinstance(other, Sun):
            print(f"\n[СОБЫТИЕ] {self.symbol} наступил на Солнце! Получено немного ресурсов (HP +10).")
            self.hp += 10
            return self
            
        elif isinstance(other, Lawnmower):
            print(f"\n[СОБЫТИЕ] {self.symbol} активировал Газонокосилку! Она сносит все на своем пути.")
            return self
            
        elif isinstance(other, Grave):
            if "Zombie" in self.__class__.__name__:
                print(f"\n[СОБЫТИЕ] Зомби {self.symbol} вылез из Могилы! Восстановлено 50 HP.")
                self.hp += 50
            else:
                print(f"\n[СОБЫТИЕ] {self.symbol} не может взаимодействовать с могилой.")
            return self
            
        elif isinstance(other, Wheelbarrow):
            print(f"\n[СОБЫТИЕ] {self.symbol} наткнулся на Тачку. Проход заблокирован!")
            return self
            
        return NotImplemented 

    unit_class.__add__ = __add__
    return unit_class