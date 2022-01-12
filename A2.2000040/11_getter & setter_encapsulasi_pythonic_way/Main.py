class Hero :

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

sarbud = Hero("sarbud", 100, 40)

print("\nMerubah info")
print(sarbud.info)
sarbud.name = "sardun"
print(sarbud.info)

print("\nGetter dan Setter untuk __armor : ")
print(sarbud.armor)
sarbud.armor = 50
print(sarbud.armor)

print("\nDelete Armor : ")
del sarbud.armor
print(sarbud.__dict__)