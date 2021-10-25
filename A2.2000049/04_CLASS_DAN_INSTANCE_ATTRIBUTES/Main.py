class heroDota:

    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroDota.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

heroPertama = heroDota("axe", 100, 78, 80)
print(heroDota.jumlah)
heroKedua = heroDota("oracle", 100, 67, 20)
print(heroDota.jumlah)
heroKetiga = heroDota("bristleback", 100, 79, 82)
print(heroDota.jumlah)