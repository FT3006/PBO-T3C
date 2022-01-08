class HeroMobileLegends :

  def __init__(self, name, health) :
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

Gatotkaca = HeroMobileLegends('Gatotkaca', 100)
Franco = Hero_Tank('Franco', 200)
Barats = Hero_Fighter('Barats', 100)
Lancelot = Hero_Assassin('Lancelot', 80)
Lylia = Hero_Mage('Lylia', 60)

print(Gatotkaca.__dict__)
print(help(Franco))
print(Barats.name)
print(Lancelot.name)
print(Lylia.name)