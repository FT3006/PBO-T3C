class Hero : #template
  #class variable
  jumlah = 0

  def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    #instance variable
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor

    Hero.jumlah += 1
    print("membuat Hero dengan nama " + inputName)

hero1 = Hero("zilong",100, 10, 5)
print(Hero.jumlah)
hero2 = Hero("miya",100, 15, 8)
print(Hero.jumlah)
hero3 = Hero("nana",100, 20, 10)
print(Hero.jumlah)