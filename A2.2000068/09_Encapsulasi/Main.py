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
Yve = HeroMobileLegends("Yve", 100, 90)

#Game Berjalan
print(Yve.getName())
print(Yve.getHealth())
Yve.diserang(20)
print(Yve.getHealth())