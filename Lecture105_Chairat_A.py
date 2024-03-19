class vehicle:
    licenseCode = ""
    serialCode = ""
    def turn_on_ac(self):
        print("Turned on: Air Conditioner")

class car(vehicle):
    def sayHi(self):
        print("Oh, Hi")

class pickup(vehicle):
    pass

class van(vehicle):
    pass

class estate(vehicle):
    pass

car1 = car()
car1.turn_on_ac()
car1.sayHi()

pickup1 = pickup()
pickup1.turn_on_ac()

van1 = van()
van1.turn_on_ac()

estate1 = estate()
estate1.turn_on_ac()