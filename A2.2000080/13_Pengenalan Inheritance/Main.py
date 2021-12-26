class HeroMobileLegends :

  def _init_(self, name, health) :
    self.name = name
    self.health = health

class Hero_Tank(HeroMobileLegends):
    pass

class Hero_Fighter(HeroMobileLegends):
    pass

class Hero_Assassin(HeroMobileLegends):
    pass

class Hero_Mage(HeroMobileLegends):
    pass

Masha = HeroMobileLegends('Masha', 100)
Uranus = Hero_Tank('Uranus', 200)
Chou = Hero_Fighter('Chou', 100)
Fanny = Hero_Assassin('Fanny', 80)
Selena = Hero_Mage('Selena', 60)

print(Masha._dict_)
print(help(Uranus))
print(Chou.name)
print(Fanny.name)
print(Selena.name)