class superCar: #template
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputMerk, inputCC, inputTorque):
        self.name = inputName
        self.merk = inputMerk
        self.cc = inputCC
        self.torque = inputTorque
        superCar.jumlah += 1
        print("Membuat superCar dengan nama " + inputName)


supercarpertama = superCar("Enzo","Ferari", 1000, 100)
print(superCar.jumlah)
supercarkedua = superCar("BMWX3","BMW", 1500, 200)
print(superCar.jumlah)
supercarketiga = superCar("Huracan","Galardo", 2000, 300)
print(superCar.jumlah)
