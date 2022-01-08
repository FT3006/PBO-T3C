class hero: # template
    # class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        hero.jumlah += 1
        print(" membuat hero dengan nama " + inputName)

hero1 = hero("udin",100, 10, 5)
print(hero.jumlah)
hero2 = hero("tatang",100, 15, 3)
print(hero.jumlah)
hero3 = hero("aldo",100, 30, 1)
print(hero.jumlah)