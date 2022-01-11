class Hero :
  #class variable
  jumlah_hero = 0

  def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor

    Hero.jumlah_hero += 1

  #Void Function, Method tanpa return dan tanpa Argumen
  def nama(self):
    print("Namaku adalah " + self.name)

  #Method dengan Argumen, tanpa return
  def healthUp(self,up):
    self.health += up

  #Method dengan return
  def getHealth(self):
    return self.health
  

hero1 = Hero('lingling', 150, 7, 2)
hero2 = Hero('sarbud', 100, 6, 3)

hero1.nama()
hero2.nama()
hero1.healthUp(2)
hero2.healthUp(9)

print(hero1.getHealth())
print(hero2.getHealth())