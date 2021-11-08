class Hero:
 #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat Hero dengan nama " + inputName)

hero1 = Hero("abayt", 100, 78, 80)
print(Hero.jumlah)
hero2  = Hero("fauzi", 100, 90, 20)
print(Hero.jumlah)
hero3  = Hero("akbar", 150, 75, 78)
print(Hero.jumlah)