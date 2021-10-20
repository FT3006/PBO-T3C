class Hero:

    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputHealth
        self.armor = inputArmor

hero1 = Hero("Gusion",100, 10, 4)
hero2 = Hero("Ling",100, 15, 1)
hero3 = Hero("Hayabusa",1000, 100, 0)

print(hero1.__dict__)
print(hero2.armor)
print(hero3.health) 