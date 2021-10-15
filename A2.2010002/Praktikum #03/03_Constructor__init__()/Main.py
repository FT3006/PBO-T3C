class superCar:
    def __init__(self, inputName, inputMerk, inputCC, inputTorque):
        self.name = inputName
        self.merk = inputMerk
        self.cc = inputCC
        self.torque = inputTorque

supercarpertama = superCar("Enzo","Ferari", 100, 1500)

print(supercarpertama.__dict__)