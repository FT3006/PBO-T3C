class Hero: #template
    #class variabel
    jumalah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputNama)


hero1 = Hero("amily",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("airi",100, 10, 5)
print(Hero.jumlah)
hero3 = Hero("sinestrea",1000, 5, 20)
print(Hero.jumlah)