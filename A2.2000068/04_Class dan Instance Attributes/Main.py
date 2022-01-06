class HeroMobileLegends : #template
  #class variable
  jumlah = 0

  def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    #instance variable
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor

    HeroMobileLegends.jumlah += 1
    print("membuat Hero dengan nama " + inputName)

hero1 = HeroMobileLegends("Gusion",100, 10, 5)
print(HeroMobileLegends.jumlah)
hero2 = HeroMobileLegends("Ling",100, 15, 8)
print(HeroMobileLegends.jumlah)
hero3 = HeroMobileLegends("Hayabusa",100, 20, 10)
print(HeroMobileLegends.jumlah)