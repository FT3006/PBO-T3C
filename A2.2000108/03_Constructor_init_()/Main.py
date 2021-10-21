class heroDota:
    def _init_(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

heroPertama = heroDota("dilabedil", 100, 78, 80)
heroKedua = heroDota("cacamarica", 150, 67, 20)
heroKetiga = heroDota("abdurh", 100, 75, 78)
print(heroPertama._dict_)
print(heroKedua._dict_)
print(heroKetiga._dict_)
