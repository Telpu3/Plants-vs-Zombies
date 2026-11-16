from abc import ABC, abstractmethod
from landscape import mixin_interaction

# Базовый интерфейс для всех юнитов
class Unit(ABC):
    def __init__(self, x, y, hp, armor, attack, symbol):
        self.x = x
        self.y = y
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.symbol = symbol

    @abstractmethod
    def move(self, new_x, new_y):
        pass

    def take_damage(self, damage):
        real_damage = max(1, damage - self.armor)
        self.hp -= real_damage
        print(f"Юнит {self.symbol} получил {real_damage} урона. HP: {self.hp}")
        if self.hp <= 0:
            print(f"Юнит {self.symbol} погиб!")
    def use_ability(self, board):
        print(f"У юнита {self.symbol} нет особых способностей.")
        
# --- Тип 1: Растения-стрелки ---
class Peashooter(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, hp=50, armor=2, attack=20, symbol='🌱')
    def move(self, new_x, new_y): self.x, self.y = new_x, new_y
    def use_ability(self, board):
        print(f"[СПОСОБНОСТЬ] 🌱 Горохострел выпускает залп по всем зомби!")
        for unit in board.units:
            if "Zombie" in unit.__class__.__name__:
                unit.take_damage(self.attack)
                print(f"Зомби {unit.symbol} получил урон от залпа!")

class SnowPea(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, hp=60, armor=3, attack=15, symbol='❄️')
    def move(self, new_x, new_y): self.x, self.y = new_x, new_y
    def use_ability(self, board):
        print(f"[СПОСОБНОСТЬ] ❄️ Снежный горох замораживает врагов!")
        for unit in board.units:
            if "Zombie" in unit.__class__.__name__:
                unit.attack = max(1, unit.attack - 5)
                print(f"Атака зомби {unit.symbol} снижена до {unit.attack}!")
# --- Тип 2: Зомби-танки ---
@mixin_interaction
class BasicZombie(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, hp=100, armor=1, attack=10, symbol='🧟')
    def move(self, new_x, new_y): self.x, self.y = new_x, new_y
    def use_ability(self, board):
        print(f"[СПОСОБНОСТЬ] 🧟 Зомби кусает воздух и восстанавливает 20 HP!")
        self.hp += 20
@mixin_interaction
class BucketZombie(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, hp=200, armor=10, attack=15, symbol='🪣')
    def move(self, new_x, new_y): self.x, self.y = new_x, new_y

# --- Тип 3: Спецназ ---
class PotatoMine(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, hp=30, armor=0, attack=100, symbol='🥔')
    def move(self, new_x, new_y): self.x, self.y = new_x, new_y

@mixin_interaction
class FootballZombie(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, hp=150, armor=5, attack=25, symbol='🏈')
    def move(self, new_x, new_y): self.x, self.y = new_x, new_y