from game import Board
from units import Peashooter, BasicZombie, SnowPea, BucketZombie
from task4 import UnitTracker
from base import Base
import random

def main():
    print("=== 🌻 PLANTS VS ZOMBIES: CONSOLE EDITION 🧟 ===")
    
    # Создаем поле и базу
    board = Board(10, 10)

    # Рисуем дом
    for y in range(10):
        board.grid[y][0] = '🏠'
    plant_base = Base("Дом Растений", hp=1000, max_units=10)
    
    # Создаем стартовых юнитов
    p1 = Peashooter(1, 2)
    z1 = BasicZombie(8, 2)
    
    UnitTracker("Peashooter")
    UnitTracker("Zombie")
    
    board.add_unit(p1)
    board.add_unit(z1)
    
    while True:
        print("\n" + "="*30)
        board.display()
        
        # Главное меню 
        print("1 - Управление базой")
        print("2 - Управление юнитом")
        print("3 - Загрузить игру")
        print("4 - Сохранить игру")
        print("5 - Новый зомби")
        print("6 - Конец хода")
        print("7 - Закончить игру")
        
        choice = input("\nВыбор: ")
        
        if choice == '7':
            print("Игра завершена!")
            break
            
        elif choice == '1':
            # Меню управления 
            print("\n--- УПРАВЛЕНИЕ БАЗОЙ ---")
            print("1 - Состояние базы")
            print("2 - Создание юнита")
            sub_choice = input("Выбор действия: ")
            
            if sub_choice == '1':
                plant_base.show_status()
            elif sub_choice == '2':
                print("1 - Горохострел (🌱)")
                print("2 - Снежный горох (❄️)")
                unit_choice = input("Выбор типа юнита: ")
                
                if unit_choice == '1':
                    new_unit = Peashooter(2, 2) # Создаем на координатах 2,2
                    plant_base.create_unit(new_unit, board)
                    UnitTracker("Peashooter")
                elif unit_choice == '2':
                    new_unit = SnowPea(3, 3) # Создаем на координатах 3,3
                    plant_base.create_unit(new_unit, board)
                    UnitTracker("SnowPea")
                    
        elif choice == '2':
            # Меню управления юнитом
            plants = [u for u in board.units if "Zombie" not in u.__class__.__name__]
            if not plants:
                print("На поле нет ваших растений!")
                continue # Возвращаемся в главное меню
            print("\n--- ВАШИ РАСТЕНИЯ ---")
            for i, plant in enumerate(plants):
                print(f"{i} - {plant.symbol} (HP: {plant.hp}) в координатах ({plant.x}, {plant.y})")
            
            try:
                selected_idx = int(input("Выберите номер растения: "))
                if selected_idx < 0 or selected_idx >= len(plants):
                    print("Неверный номер!")
                    continue
                
                selected_plant = plants[selected_idx]
                
                # Теперь работаем с выбранным растением!
                print(f"\nВыбран юнит {selected_plant.symbol}.")
                print("1 - Перемещение")
                print("2 - Использование способности")
                sub_choice = input("Выбор действия: ")
                
                if sub_choice == '1':
                    try:
                        new_x = int(input("Введите новую координату X (0-9): "))
                        new_y = int(input("Введите новую координату Y (0-9): "))
                        if 0 <= new_x < board.width and 0 <= new_y < board.height:
                            board.remove_unit(selected_plant)
                            selected_plant.move(new_x, new_y)
                            board.add_unit(selected_plant)
                        else:
                            print("Ошибка: координаты за пределами поля!")
                    except ValueError:
                        print("Ошибка: нужно вводить числа!")
                elif sub_choice == '2':
                    selected_plant.use_ability(board)
                    # Очищаем поле от погибших зомби
                    for unit in list(board.units):
                        if unit.hp <= 0:
                            board.remove_unit(unit)
            except ValueError:
                print("Ошибка: нужно ввести число.")       

        elif choice == '3':
            UnitTracker.load_from_json()
            
        elif choice == '4':
            UnitTracker.save_to_json()
            
        elif choice == '5':
            for _ in range(100): 
                rx = random.randint(0, 9)
                ry = random.randint(0, 9)
                if board.get_unit_at(rx, ry) is None:
                    if random.random() > 0.5:
                        new_z = BasicZombie(rx, ry)
                    else:
                        new_z = BucketZombie(rx, ry)
                    board.add_unit(new_z)
                    UnitTracker("Zombie")
                    print(f"На поле появился новый зомби в координатах ({rx}, {ry})!")
                    break 

        elif choice == '6':
            print("\n[ХОД ЗОМБИ] Зомби начинают движение...")
            for unit in list(board.units):
                if "Zombie" in unit.__class__.__name__:
                    if unit.x >= 0:
                        target = board.get_unit_at(unit.x - 1, unit.y)
                        
                        if target is None:
                            board.remove_unit(unit)
                            unit.move(unit.x - 1, unit.y)
                            board.add_unit(unit)
                            print(f"Зомби {unit.symbol} шагнул на клетку влево (X={unit.x}).")
                        elif "Zombie" not in target.__class__.__name__:
                            print(f"Зомби {unit.symbol} атакует растение {target.symbol}!")
                            target.take_damage(unit.attack)
                            if target.hp <= 0:
                                board.remove_unit(target)
                                print(f"Растение {target.symbol} уничтожено зомби!")
                        else:
                            print(f"Зомби {unit.symbol} не может пройти, там другой зомби.")
            print("[ХОД ЗОМБИ] Все зомби сделали ход.")
            
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()