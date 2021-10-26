class superCar: #template
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputMerk, inputCC, inputTorque):
        self.name = inputName
        self.merk = inputMerk
        self.cc = inputCC
        self.torque = inputTorque
        superCar.jumlah += 1

# void function, method tanpa return, tanpa argumen
    def apa(self):
        print(" Nama Mobil Adalah " + self.name)

# method dengana rgumen, tanpa return
    def ccUp(self, up):
        self.cc +=up

# void function, method tanpa return, tanpa argumen
    def getCc(self):
        return self.cc


supercar1 = superCar('Enzo','Ferari', 1000, 450)

supercar1.apa()
supercar1.ccUp(1000)

print(supercar1.getCc())
