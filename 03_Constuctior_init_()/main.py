class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("abay", 100, 78, 80)
hero2   = Hero("fauzi", 100, 90, 20)
hero3  = Hero("akabr", 150, 75, 78)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)