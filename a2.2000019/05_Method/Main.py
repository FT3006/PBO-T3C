class Hero:
    #class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
     self.name = inputName 
     self.health = inputHealth
     self.power = inputPower
     self.armor = inputArmor
     Hero.jumlah_hero += 1 

    # void function, method tanpa return, tanpa arguen
    def siapa(self):
        print("namaku adalah " + self.name)

    # method dengan argumen, tanpa return
    def healthUp(self,Up):
        self.health += Up

    # method dengan return
    def getHealth(self):
         return self.health


hero1 = Hero("Badang",100, 10, 5)
hero2 = Hero("Roger", 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())