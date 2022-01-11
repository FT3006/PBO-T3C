class Hero :
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
    attackDiterima = attackPowerLawan/self.armorNumber
    print('Serangan diterima = ' + str(attackDiterima))
    self.health -= attackDiterima
    print('HP ' + self.name + ' tersisa ' + str(self.health))

lingling = Hero('lingling', 10, 9, 8)
sarbud = Hero('sarbud', 10, 9, 8)

print('\nPotret EXP lane =\n')
sarbud.serang(lingling)
print('\n')
lingling.serang(sarbud)
print('\n')
lingling.serang(sarbud)
print('\n')
lingling.serang(sarbud)
print('\n')
lingling.serang(sarbud)
print('\n')
lingling.serang(sarbud)
print('\n')
lingling.serang(sarbud)
print('\n')
sarbud.serang(lingling)
print('\n')
sarbud.serang(lingling)
print('\n')
sarbud.serang(lingling)