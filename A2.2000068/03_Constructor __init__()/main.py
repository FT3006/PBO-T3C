class Hero: #template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
      self.name = inputName
      self.health = inputHealth
      self.power = inputPower
      self.armor = inputArmor


hero1 = Hero("Gusion", 100, 100, 50)
hero2 = Hero("Ling", 100, 50, 100)
hero3 = Hero("Hayabusa", 100, 80, 100)

print(hero1.__dict__)
print(hero2.power)
print(hero3.armor)

