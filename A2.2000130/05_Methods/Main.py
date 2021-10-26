class HunterXHunter:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        HunterXHunter.jumlah_hero += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("namaku adalah " + self.name)

    # method dengan argumen, tanpa return
    def healthUp(self,Up):
        self.health += Up
    
    # method dengan return 
    def getHealth(self):
        return self.health


hero1 = HunterXHunter('Gon', 100, 20, 3)
hero2 = HunterXHunter('Killua', 100, 13, 5)

hero1.siapa()
hero1.healthUp(15)

print(hero1.getHealth())