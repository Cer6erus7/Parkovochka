from main import Car, Parking
from pprint import pprint


text = """
Welcome on Parking! What do you want to do?
A - add your car
B - check all cars on parking
C - check info about every car
D - remove car from parking
E - free space on parking
F - exit"""

park = Parking()

def viz_del(id, tuple):                                 # Функция для проверки машини на стоянке и отвечает в зависимости от наличии машины на парковке
    for i in tuple:
        if id == i[1]:
            park.delete_car(id)
            return "Car was removed"
    return "Car is not on parking"


# ________________________Menu________________________________

while True:                                                 # Запуск меню парковки
    print(text)
    choice = input(">>> ").upper()


    if "A" in choice[0]:                                        # Добавление машини на парковку
        name = input("\nType name of your car - ")
        try:
            name_of_car = Car(name)
            tuple_of_car = name_of_car.get_tuple()
            dict_of_car = name_of_car.get_dict()
            start_time = name_of_car.get_time()

            park.add_car(tuple_of_car, dict_of_car)
            park.add_id_time(start_time)
            print("Car was added")
        except:                                                 # Если парковка полна
            print("Parking is full")

    elif "B" in choice[0]:                                          # Проверка всех машин на стоянке
        print(park.info_of_available_cars())

    elif "C" in choice[0]:                                          # Информация обо всех машинах на парковке
        pprint(park.info_dict_car(), indent=2)

    elif "D" in choice[0]:                                                # Удаление машины с паркови
        try:
            cars_id = int(input("\nType ID of the car what you want to remove - "))
            tuplik = park.info_of_available_cars()

            print(viz_del(cars_id, tuplik))
        except:
            print("Invalid ID")

    elif "E" in choice[0]:                                                 # Проверка оставшихся мест на парковке
        remaind = park.left_space()
        print(f"Free space - {remaind}")

    elif "F" in choice[0]:                                                 # Выход из меню
        print("Goodbye!")
        break