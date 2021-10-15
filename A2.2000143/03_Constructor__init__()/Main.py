class heroValoran:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

heroPertama = heroValoran("raze", 1000, 75, 80)
heroKedua = heroValoran("brimstone", 1500, 85, 20)
heroKetiga = heroValoran("sage", 2500, 95, 78)
print(heroPertama.__dict__)
print(heroKedua.__dict__)
print(heroKetiga.__dict__)