import datetime


class Car:                         # Клас машина
    def __init__(self, name):                 # Инициализация всех нужных данных
        self.name = name
        self.id = id(self.name)
        self.start_time = datetime.datetime.now()
        self.on_park = True

    def get_tuple(self):                            # метод для конвертации названия машины и её айди в tuple для передачи в клас Parking
        tuplik = self.name, self.id
        return tuple(tuplik)

    def get_dict(self):                                   # метод для конвертации уже всех данных для удобного просматривания и передачи в Parking
        self.time_when_active = self.start_time.strftime("%H:%M:%S")
        return {self.id: {"Brand": self.name, "Start time": self.time_when_active, "End time": None, "Status on Parkovochka": True, "How long car stayed": None}}

    def get_time(self):                              # метод для конвертации данные времени для передачи в класс Parking
        return {self.id: self.start_time}


class Parking:                                              # Клас парковки
    def __init__(self, max_capacity = 5):                    # Инициализация всех нужных данных для парковки
        self.max_capacity = max_capacity
        self.cars = list()
        self.tickets = dict()
        self.id_time = dict()
        self.end_time = None

    def info_of_available_cars(self):                       # Метод для возвращения списка со всеми машинамы и их айди
        return self.cars

    def info_dict_car(self):                                # Метод для возращения словаря со всеми данными по каждой машине
        return self.tickets

    def add_car(self, get_tuple, get_dict):                 # Метод для добавления словаря и тюпла в этот класс, если места на парвке ещё есть
        if len(self.cars) < self.max_capacity:
            self.cars.append(get_tuple)
            self.tickets.update(get_dict)
        else:
            raise "Parking is full"

    def add_id_time(self, get_time):                         # Метод для добавления времени начала
        self.id_time.update(get_time)

    def left_space(self):                                       # Метод возвращает количество свободных мест
        return self.max_capacity - len(self.cars)

    def delete_car(self, id):                                           # Метод для удаления машины со стоянки и изминения её статуса в словаре
        for i in self.cars:
            if i[1] == id:
                self.end_time = datetime.datetime.now()
                end_time = self.end_time.strftime("%H:%M:%S")
                time_on_parkovochka = self.end_time - self.id_time[id]

                self.tickets[id]["End time"] = end_time
                self.tickets[id]["Status on Parkovochka"] = False
                self.tickets[id]["How long car stayed"] = f"{time_on_parkovochka.seconds} sec"
                self.cars.remove(i)