class heroAvenger:
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroAvenger.jumlah += 1
        print("Membuat hero dengan nama " + inputName)


hero1 = heroAvenger("Ironman",100, 10, 4)
print(heroAvenger.jumlah)
hero2 = heroAvenger("Blackwidow",100, 15, 1)
print(heroAvenger.jumlah)
hero3 = heroAvenger("wakanda",1000, 100, 0)
print(heroAvenger.jumlah)