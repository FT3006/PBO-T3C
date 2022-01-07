class HeroMobileLegends :
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

Chou = HeroMobileLegends('Chou', 10, 9, 8)
Paquito = HeroMobileLegends('Paquito', 10, 9, 8)

print('\nPotret EXP lane =\n')
Chou.serang(Paquito)
print('\n')
Paquito.serang(Chou)
print('\n')
Paquito.serang(Chou)
print('\n')
Paquito.serang(Chou)
print('\n')
Paquito.serang(Chou)
print('\n')
Paquito.serang(Chou)
print('\n')
Paquito.serang(Chou)
print('\n')
Chou.serang(Paquito)
print('\n')
Chou.serang(Paquito)
print('\n')
Chou.serang(Paquito)