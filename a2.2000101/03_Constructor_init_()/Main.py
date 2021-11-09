class heroleagueoflegends:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

heroPertama = heroleagueoflegends("Ahri", 100, 78, 70)
heroKedua = heroleagueoflegends("Alistar", 150, 87, 30)
heroKetiga = heroleagueoflegends("Braum", 200, 95, 68)
print(heroPertama.__dict__)
print(heroKedua.__dict__)
print(heroKetiga.__dict__)