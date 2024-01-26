class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    def Carry(self):
        print("carry up")
    
class Car(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

color = ""
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
pickup1.Carry()
pickup1.color = "red"


Car1 = Car()
Car1.turnOnAirConditioner()

Van1 = Van()
Van1.turnOnAirConditioner()

Estatecar1 = Estatecar()
Estatecar1.turnOnAirConditioner()
