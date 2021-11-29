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
    def siapa(self):
        print("my name is " + self.name)

    # method dengan argumen, tanpa return
    def powerUp(self, up):
        self.power +=up
    
    # method dengan return
    def getPower(self):
        return self.power
        

hero1 = hero("wandi", 1000, 125, 120)
hero2 = hero("aldos",1000, 120, 125)

hero1.siapa()
hero1.powerUp(20)

print(hero1.getPower())

hero2.siapa()
hero2.powerUp(30)

print(hero2.getPower())