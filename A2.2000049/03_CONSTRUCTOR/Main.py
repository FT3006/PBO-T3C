class heroDota:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

heroPertama = heroDota("axe", 100, 78, 80)
heroKedua = heroDota("oracle", 100, 67, 20)
heroKetiga = heroDota("undying", 100, 75, 78)
print(heroPertama.__dict__)
print(heroKedua.__dict__)
print(heroKetiga.__dict__)