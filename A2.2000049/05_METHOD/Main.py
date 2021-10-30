class heroDota:
    #class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroDota.jumlah_hero += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("namaku adalah " + self.name)

    #method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up

    #method dengan return
    def getHealth(self):
        return self.health

hero1 = heroDota('axe', 100, 80, 90)
hero2 = heroDota('monkey king', 100, 80, 60)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
    

