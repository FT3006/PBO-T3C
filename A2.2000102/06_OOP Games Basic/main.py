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

zilong = Hero('zilong', 10, 9, 8)
miya = Hero('miya', 10, 9, 8)

print('\nPotret EXP lane =\n')
zilong.serang(miya)
print('\n')
zilong.serang(miya)
print('\n')
zilong.serang(miya)
print('\n')
zilong.serang(miya)
print('\n')
zilong.serang(miya)
print('\n')
zilong.serang(miya)
print('\n')
zilong.serang(miya)
print('\n')
miya.serang(zilong)
print('\n')
miya.serang(zilong)
print('\n')
miya.serang(zilong)