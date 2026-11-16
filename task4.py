import json

class UnitTracker:
    """
    Класс-счетчик (Вариант 13).
    Подсчитывает количество созданных экземпляров.
    Перегружает метод __del__ для уменьшения счетчика при удалении.
    Умеет сохранять и загружать данные в JSON.
    """
    
    # Статическая переменная класса (общая для всех экземпляров)
    _count = 0

    def __init__(self, name):
        self.name = name
        # При создании нового объекта увеличиваем общий счетчик
        UnitTracker._count += 1
        print(f"[СЧЕТЧИК] Создан объект '{self.name}'. Всего объектов: {UnitTracker._count}")

    def __del__(self):
        """
        Перегрузка деструктора (вызывается при удалении объекта).
        Уменьшает общий счетчик.
        """
        UnitTracker._count -= 1
        print(f"[СЧЕТЧИК] Объект '{self.name}' уничтожен. Осталось объектов: {UnitTracker._count}")

    @classmethod
    def get_count(cls):
        """Возвращает текущее кол-во объектов"""
        return cls._count

    @classmethod
    def save_to_json(cls, filename="units_data.json"):
        """Сохраняет текущее состояние счетчика в JSON-файл"""
        data = {
            "total_objects": cls._count,
            "class_name": cls.__name__
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"[СОХРАНЕНИЕ] Данные записаны в файл {filename}")

    @classmethod
    def load_from_json(cls, filename="units_data.json"):
        """Загружает данные о счетчике из JSON-файла"""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                cls._count = data.get("total_objects", 0)
                print(f"[ЗАГРУЗКА] Данные восстановлены из {filename}. Объектов: {cls._count}")
        except FileNotFoundError:
            print(f"[ОШИБКА] Файл {filename} не найден. Счетчик остается равным {cls._count}")
        except json.JSONDecodeError:
            print(f"[ОШИБКА] Файл {filename} поврежден или пуст.")

#Тестирование
if __name__ == "__main__":
    print("--- Тестируем счетчик ---")
    
    # Создаем объекты
    unit1 = UnitTracker("Горохострел")
    unit2 = UnitTracker("Зомби")
    
    print(f"Текущий счетчик: {UnitTracker.get_count()}")
    
    # Сохраняем в файл
    UnitTracker.save_to_json()
    
    # Удаляем один объект (сработает __del__)
    print("\nУдаляем один объект...")
    del unit1
    
    print(f"Текущий счетчик после удаления: {UnitTracker.get_count()}")
    
    # Сбрасываем счетчик и загружаем из файла
    print("\nЗагружаем из файла...")
    UnitTracker.load_from_json()