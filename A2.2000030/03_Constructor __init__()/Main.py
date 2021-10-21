class Hero: #template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("amily",100, 10, 4)
hero2 = Hero("airi",100, 10, 5)
hero3 = Hero("sinestrea",1000, 5, 20)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)