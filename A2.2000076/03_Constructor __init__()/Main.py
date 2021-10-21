class heroMarvel:
    def __init__(self, inputName, inputHP, inputPower, inputArmor):
        self.name = inputName
        self.hp = inputHP
        self.power = inputPower
        self.armor = inputArmor

hero1 = heroMarvel ("Thor",120,100,80)
hero2 = heroMarvel ("Hulk",250,80,80)
hero3 = heroMarvel ("IronMan",150,100,120)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)