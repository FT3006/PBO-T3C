class hero: # template
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel

        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        hero.jumlah += 1
        print("membuat hero dengan nama" + inputName)


hero1 = hero("zilong", 100, 10, 4)
print(hero.jumlah)
hero2 = hero("miya", 100, 15, 1)
print(hero.jumlah)
hero3 = hero("nana", 1000, 100, 0)
print(hero.jumlah)
