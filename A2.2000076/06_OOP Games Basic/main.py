class Hero:

    def __init__(self,name,HP,attackPower,armorNumber):
        self.name = name
        self.HP = HP
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name )
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.HP -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.HP))

Hulk = Hero('Hulk',100,10,5)
Spiderman = Hero('Spiderman',100,20,10)

Hulk.serang(Spiderman)
print("\n")
Spiderman.serang(Hulk)
