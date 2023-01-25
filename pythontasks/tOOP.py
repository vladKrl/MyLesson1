class Car:
    def __init__(self, nameModel="T1", mark="Tesla"):
        self.nameModel = nameModel
        self.mark = mark

    def info(self):
        print("Марка машины - " + self.mark + ", название модели - " + self.nameModel + ".")

    def speed(self, speed=120):
        print("Машина марки - " + self.mark + " едет со скоростью " + str(speed) + " км/ч.")

    def __del__(self):
        print("УНИЧТОЖЕНО")

class BMW(Car):
    def __init__(self, nameModel="A1"):
        super().__init__(nameModel)

    def info(self):
        print("Название модели " + self.nameModel + ".")

    def speed(self, speed=80):
        print("Машина марки BWM едет со скоростью " + str(speed) + " км/ч.")


bmw1 = BMW()
bmw1.info()
bmw1.speed()

car1 = Car()
car1.info()
car1.speed()
del car1
