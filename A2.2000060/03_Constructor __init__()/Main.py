class Hero: #template

    def __init__(self, inputName, inputHP, inputATK, inputMATK, inputPDef, inputMDef):
        self.name = inputName
        self.hp = inputHP
        self.atk = inputATK
        self.matk = inputMATK
        self.pdef = inputPDef
        self.mdef = inputMDef

#Information Input
#Name = Hero Name
#ATK = Attack Power
#MATK = Magic Power
#HP = Hit Poit (Total Health)
#PDef = Physical Defend
#MDef = Magic Defend

hero1 = Hero("Sniper", 100, 30, 5, 4, 5)
hero2 = Hero("Mirana", 100, 15, 21, 1, 7)
hero3 = Hero("Ucup", 10000, 100, 250, 0, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)