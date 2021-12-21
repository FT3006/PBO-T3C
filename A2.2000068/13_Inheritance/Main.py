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

Alucard = HeroMobileLegends('Alucard', 100)
Tigreal = Hero_Tank('Tigreal', 200)
Barats = Hero_Fighter('Barats', 100)
Natalia = Hero_Assassin('Natalia', 80)
Pharsa = Hero_Mage('Pharsa', 60)

print(Alucard.__dict__)
print(help(Tigreal))
print(Barats.name)
print(Natalia.name)
print(Pharsa.name)