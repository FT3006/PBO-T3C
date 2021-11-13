class hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        hero.jumlah_hero += 1

    # void function, method tanpa return, tanpa argumen
    def who(self):
        print("my name is " + self.name)

    # method dengan argumen, tanpa return
    def powerUp(self, up):
        self.power +=up
    
    # method dengan return
    def getPower(self):
        return self.power
        

hero1 = hero("Naruto", 1000, 125, 120)
hero2 = hero("luffy",1000, 120, 125)

hero1.who()
hero1.powerUp(15)

print(hero1.getPower())

hero2.who()
hero2.powerUp(25)

print(hero2.getPower())