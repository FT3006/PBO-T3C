class heroMarvel:
    #class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHP, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.HP = inputHP
        self.power = inputPower
        self.armor = inputArmor
        heroMarvel.jumlah_hero += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("Namaku adalah " + self.name)

    #method dengan argumen, tanpa return
    def HPUp(self,up):
        self.HP += up

    #method dengan return
    def getHP(self):
        return self.HP

hero1 = heroMarvel("Thor",120,100,80)
hero2 = heroMarvel("Hulk",250,80,80)

hero1.siapa()
hero1.HPUp(30)
print(hero1.getHP())
