class HeroMobileLegends:

    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = HeroMobileLegends("Gusion",100, 10, 5)
hero2 = HeroMobileLegends("Ling",100, 15, 8)
hero3 = HeroMobileLegends("Hayabusa",100, 20, 10)

print(hero1.__dict__)
print(hero2.armor)
print(hero3.health) 