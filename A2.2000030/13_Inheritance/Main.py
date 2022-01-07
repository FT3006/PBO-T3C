class HeroAOV :

  def __init__(self, name, health) :
    self.name = name
    self.health = health

class Hero_Tank(HeroAOV):
    pass

class Hero_Warrior(HeroAOV):
    pass

class Hero_Assassin(HeroAOV):
    pass

class Hero_Mage(HeroAOV):
    pass

Arum = HeroAOV('Arum', 100)
Mina = Hero_Tank('Mina', 200)
Airi = Hero_Warrior('Airi', 100)
Sinestrea = Hero_Assassin('Sinestrea', 80)
Liliana = Hero_Mage('Liliana', 60)

print(Arum.__dict__)
print(help(Mina))
print(Airi.name)
print(Sinestrea.name)
print(Liliana.name)