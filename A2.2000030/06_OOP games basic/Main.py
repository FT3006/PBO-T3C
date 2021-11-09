class Hero: 

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

def serang(self, lawan):
    print(self.name + ' menyerang ' + lawan.name )
    lawan.deserang(self, self.attackPower)

def diserang(self, lawan, attackPower_lawan):
    print(self.name + ' diserang ' + lawan.name)
    attack_diterima = attackPower_lawan/self.armornumber
    print('serang terasa : ' + str(attack_diterima))
    self.health -= attack_diterima
    print('darah ' + self.name + ' tersisa ' + str(self.health))

rama = Hero('rama',200,20,5)
bima = Hero('bima',200,30,10)

rama.serang(bima)
print("\n")