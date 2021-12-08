class Hero:
    #class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    #Void Function, Method Tanpa Return, Tanpa Argumen
    def siapa(self):
        print("Namaku adalah " + self.name)

    #Method Dengan Argumen, Tanpa Return
    def healthUp(self,up):
        self.health += up

    #Method Dengan Return
    def getHealth(self):
        return self.health

herol = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

herol.siapa()
herol.healthUp(10)

print(herol.getHealth())