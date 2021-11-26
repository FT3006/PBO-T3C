class HeroMobileLegends :
  
  def __init__(self, name, health, attackPower):
    self.__name = name
    self.__health = health
    self.__attackPower = attackPower

  #getter
  def getName(self):
    return self.__name

  def getHealth(self):
    return self.__health

  #setter
  def diserang(self, damageMasuk):
    self.__health -= damageMasuk

  def setAttPower(self, nilaiBaru):
    self.__attPower = nilaiBaru

#Awal Game
Hayabusa = HeroMobileLegends("Hayabusa", 100, 90)

#Game Berjalan
print(Hayabusa.getName())
print(Hayabusa.getHealth())
Hayabusa.diserang(20)
print(Hayabusa.getHealth())