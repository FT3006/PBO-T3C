class hero: # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = hero("wadin",100, 10, 5)
hero2 = hero("gp",100, 20, 5)
hero3 = hero("kyy",100, 25, 2)
hero3 = hero("ponge",100, 12, 5)
hero4 = hero("zm",100, 15, 7)
hero5 = hero("Lpyy",100, 12, 7)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)
print(hero5.__dict__)