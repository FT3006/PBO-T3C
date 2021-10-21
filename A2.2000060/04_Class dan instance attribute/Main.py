class Hero: #template
    #class variable
    jumlah = 0

    def __init__(self, inputName, inputHP, inputATK, inputMATK, inputPDef, inputMDef):
        #instance variable
        self.name = inputName
        self.hp = inputHP
        self.atk = inputATK
        self.matk = inputMATK
        self.pdef = inputPDef
        self.mdef = inputMDef
        Hero.jumlah += 1
        print("Membuat Hero dengan nama " + inputName)

#Information Input
#Name = Hero Name
#ATK = Attack Power
#MATK = Magic Power
#HP = Hit Poit (Total Health)
#PDef = Physical Defend
#MDef = Magic Defend

hero1 = Hero("Sniper", 100, 30, 5, 4, 5)
print(Hero.jumlah)
hero2 = Hero("Mirana", 100, 15, 21, 1, 7)
print(Hero.jumlah)
hero3 = Hero("Ucup", 10000, 100, 250, 0, 0)
print(Hero.jumlah)