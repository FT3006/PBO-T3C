class Hero: #template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("lingling",150, 7, 2)
hero2 = Hero("sarbud",100, 6, 3)
hero3 = Hero("koeni",200, 4, 1)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)