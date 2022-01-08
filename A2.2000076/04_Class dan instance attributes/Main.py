class heroMarvel:
    #class variabel
    jumlah = 0

    def __init__(self, inputName, inputHP, inputPower, inputArmor):
        #instance variabel
        self.name = inputName
        self.HP = inputHP
        self.power = inputPower
        self.armor = inputArmor

        heroMarvel.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

hero1 = heroMarvel("Thor",120,100,80)
print(heroMarvel.jumlah)
hero2 = heroMarvel("Hulk",250,80,80)
print(heroMarvel.jumlah)
hero3 = heroMarvel("IronMan",150,100,120)
print(heroMarvel.jumlah) 