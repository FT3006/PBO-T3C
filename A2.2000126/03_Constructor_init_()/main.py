class hero: # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = hero("ripan",100, 10, 5)
hero2 = hero("alfi",100, 20, 5)
hero3 = hero("stev",1000, 125, 2)


print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
