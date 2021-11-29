class Hero:

    def __init__(self, name, Healt, attackPower, armorNumber):
        self.name = name
        self.health = Healt
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' Menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' Diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('Serangan yang di dapatkan ' + self.name + ' sebesar ' + str(attack_diterima))
        self.health -= attack_diterima
        print('Darah ' + self.name + ' yang tersisa sebanyak ' + str(self.health))

sniper = Hero('Sniper', 100, 10, 5)
rikimaru = Hero('Rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)