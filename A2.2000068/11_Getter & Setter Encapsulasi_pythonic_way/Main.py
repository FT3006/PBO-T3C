class HeroMobileLegends :

  def __init__(self, name, health, armor) :
    self.name = name
    self.__health = health
    self.__armor = armor

#self.info = "name {} : \n\t health : {}".format(self.name, self.__health)

  @property
  def info(self):
    return "name {} : \n\t health : {}".format(self.name, self.__health)

  @property
  def armor(self):
    pass

  @armor.getter
  def armor(self):
    return self.__armor

  @armor.setter
  def armor(self, input):
    self.__armor = input

  @armor.deleter
  def armor(self):
    print("Armor telah di Hapus")
    self.__armor = None

Natan = HeroMobileLegends("Natan", 100, 40)

print("\nMerubah info")
print(Natan.info)
Natan.name = "Granger"
print(Natan.info)

print("\nGetter dan Setter untuk __armor : ")
print(Natan.armor)
Natan.armor = 50
print(Natan.armor)

print("\nDelete Armor : ")
del Natan.armor
print(Natan.__dict__)
