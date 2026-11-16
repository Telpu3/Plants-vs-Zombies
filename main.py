from game import Board
from units import Peashooter, BasicZombie, SnowPea
from task4 import UnitTracker
from base import Base

def main():
    print("=== 🌻 PLANTS VS ZOMBIES: CONSOLE EDITION 🧟 ===")
    
    # Создаем поле и базу
    board = Board(10, 10)
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
        print("5 - Закончить игру")
        
        choice = input("\nВыбор: ")
        
        if choice == '5':
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
            print("\nЮнит 🌱 готов к приказу!")
            print("1 - Перемещение")
            print("2 - Использование способности (в разработке)")
            sub_choice = input("Выбор действия: ")
            
            if sub_choice == '1':
                try:
                    new_x = int(input("Введите новую координату X (0-9): "))
                    new_y = int(input("Введите новую координату Y (0-9): "))
                    if 0 <= new_x < board.width and 0 <= new_y < board.height:
                        board.remove_unit(p1)
                        p1.move(new_x, new_y)
                        board.add_unit(p1)
                    else:
                        print("Ошибка: координаты за пределами поля!")
                except ValueError:
                    print("Ошибка: нужно вводить числа!")
            elif sub_choice == '2':
                print("Способности появятся в следующем обновлении.")
                
        elif choice == '3':
            UnitTracker.load_from_json()
            
        elif choice == '4':
            UnitTracker.save_to_json()
            
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()