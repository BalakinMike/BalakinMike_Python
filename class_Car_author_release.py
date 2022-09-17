from abc import abstractmethod


class BaseSMSSender:
    def __init__(self, server: str, port: int, login: str, pwd: str):
        self.server = server
        self.port = port
        self.login = login
        self.pwd = pwd
        if self.server and self.login and self.pwd:
            self._connect()
        else:
            print("ОШИБКА НЕТ ДАННЫХ")

    @abstractmethod
    def send_sms(self, msg: str):
        ...

    @abstractmethod
    def _connect(self):
        ...

    @abstractmethod
    def _check_server(self) -> bool:
        ...

    def health(self):
        if self._check_server():
            return "Сервер доступен, все хорошо"
        return "Сервер НЕ доступен, все плохо"


class MTSSmsSender(BaseSMSSender):
    SENDER_NAME: str = "MTS"

    def send_sms(self, msg: str):
        print(f"Отправили СМС через {self.SENDER_NAME} - {msg}")

    def _connect(self):
        print(f"Пошли и подключились - {self.server}/{self.port}@{self.login}/{self.pwd}")

    def _check_server(self) -> bool:
        return True


class TELE2SmsSender(MTSSmsSender):
    SENDER_NAME: str = "TELE2"

    def send_sms(self, msg: str):
        print("Копия вашего СМС ушла к Маме")
        print(f"INFO | Отправили СМС через {self.SENDER_NAME} - {msg}")


sender = MTSSmsSender("MTSServer", 8000, "user_1", "qweqxscdsf")
sender.send_sms("привет Мир")
check_result = sender.health()
print(check_result)

print("---------------")
sender_2 = TELE2SmsSender("TELE2Server", 7000, "user_Tele", "qweqxscdsf")
sender_2.send_sms("пока Мир")
check_result = sender_2.health()
print(check_result)


class BaseCar:
    FUEL_TYPE = "gas"
    STATUS_STOP = "STOP"
    STATUS_WORK = "WORK"

    def __init__(self):
        self.fuel_level = 0
        self.state = self.STATUS_STOP

    def __get_state(self):
        print(f"Машина находится в состоянии - {self.state}")

    def start(self):
        if self.state == self.STATUS_WORK:
            self.__get_state()
            return

        self.state = self.STATUS_WORK
        print(f"Машина переведена в статус - {self.state}")

    def stop(self):
        if self.state == self.STATUS_STOP:
            self.__get_state()
            return

        self.state = self.STATUS_STOP
        print(f"Машина переведена в статус - {self.state}")


class Car1(BaseCar):
    def __init__(self, name, color, fuel_level):
        super().__init__()
        self.state = self.STATUS_STOP
        self.name = name
        self.color = color
        self.fuel_level = fuel_level

    def add_fuel(self, value):
        self.fuel_level += value
        return self.fuel_level


class Car2(Car1):
    def beep(self):
        print("Beeeeeeeeeeeeep")



print(Car2.mro())

car = Car1("KIA", "RED", 20)
print(car.name)

car_2 = Car2("LADA", "GREEN", 120)
print(car_2.name)
car_2.beep()

park = [car, car_2]

cars_count = 0
fuel = 0
for car_obj in park:
    print(car_obj.fuel_level)
    if car_obj.fuel_level < 50:
        car_obj.add_fuel(10)
        print(f"Теперь в машине ===> {car_obj.fuel_level} топлива")

    fuel = fuel + car_obj.fuel_level
    cars_count += 1

avg = fuel / cars_count
print(f"Средне топлива в {cars_count} машинах = {avg}")
