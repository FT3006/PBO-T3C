class superCar:
    def __init__(self, inputName, inputMerk, inputCC, inputTorque):
        self.name = inputName
        self.merk = inputMerk
        self.cc = inputCC
        self.torque = inputTorque

supercarpertama = superCar("Enzo","Ferari", 1000, 100)
supercarkedua = superCar("BMWX3","BMW", 1500, 200)
supercarketiga = superCar("Huracan","Galardo", 2000, 300)

print(supercarpertama.__dict__)
print(supercarkedua.__dict__)
print(supercarketiga.__dict__)