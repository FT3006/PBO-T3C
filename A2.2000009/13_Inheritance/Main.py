class HeroGenshinImpact :

  def __init__(self, name, health) :
    self.name = name
    self.health = health

class Hero_Tank(HeroGenshinImpact):
    pass

class Hero_Fighter(HeroGenshinImpact):
    pass

class Hero_Assassin(HeroGenshinImpact):
    pass

class Hero_Mage(HeroGenshinImpact):
    pass

Ayaka = HeroGenshinImpact('Ayaka', 100)
Diluc = Hero_Tank('Diluc', 200)
Thoma = Hero_Fighter('Thoma', 100)
Hutao = Hero_Assassin('Hutao', 80)
Amber = Hero_Mage('Amber', 60)

print(Ayaka.__dict__)
print(help(Diluc))
print(Thoma.name)
print(Hutao.name)
print(Amber.name)