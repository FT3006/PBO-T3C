class heroValoran:
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroValoran.jumlah += 1
        print("Membuat hero dengan nama " + inputName)


hero1 = heroValoran("raze",100, 10, 4)
print(heroValoran.jumlah)
hero2 = heroValoran("brimstone",100, 15, 1)
print(heroValoran.jumlah)
hero3 = heroValoran("sage",1000, 100, 0)
print(heroValoran.jumlah)