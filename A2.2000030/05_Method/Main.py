class Hero:
    #class variabel
    jumalah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        
# void function, method tanpa return, tanpa argumen
def siapa(self):
    print("namaku adalah " + self.name)

# method dengan argumen, tanpa return
def healthUp(self,up):
    self.health += up

# method dengan return
def getHealth(self):
    return self.health

hero1 = Hero('amily',100, 10, 4)
hero2 = Hero('airi',100, 10, 5)
hero3 = Hero('sinestrea',1000, 5, 20)

hero1.siapa()
hero1.healthUp(10)

print(hero1.gethealth())