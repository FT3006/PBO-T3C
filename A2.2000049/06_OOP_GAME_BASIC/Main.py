class Hero:

    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPowerLawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPowerLawan/self.armorNumber
        print('serangan terasa: ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('sniper', 100, 100, 5)
axe = Hero('axe', 100, 20, 10)

sniper.serang(axe)
print("\n")
axe.serang(sniper)
print("\n")
axe.serang(sniper)
print("\n")
axe.serang(sniper)
print("\n")
axe.serang(sniper)
print("\n")
axe.serang(sniper)


