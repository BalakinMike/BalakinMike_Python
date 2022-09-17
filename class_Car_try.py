class Car:
    FUEL_TYPE = 'gas'
    STATUS_STOP = 'STOP'
    STATUS_WORK = 'WORK'

    def __init__(self, name, color):
        self.state = self.STATUS_STOP
        self.name = name
        self.color = color

    def get_state(self):
        print(f'Машина находится в состоянии - {self.state}')

    def start(self):
        if self.state == self.STATUS_WORK:
            self.get_state()
            return

        self.state = self.STATUS_WORK
        print(f'Машина переведена в состояние - {self.state}')

    def stop(self):
        if self.state == self.STATUS_STOP:
            self.get_state()
            return

        self.state = self.STATUS_STOP
        print(f'Машина переведена в состояние - {self.state}')

    def beep(self):
        ...

    def move(self):
        ...

car = Car('KIA', 'RED')
car.start()
car.get_state()
car.stop()
car.get_state()
        