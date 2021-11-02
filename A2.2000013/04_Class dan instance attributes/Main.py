class heroDota:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    jumlah = 0
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroDota.jumlah += 1
        print("membuat hero dengan nama " + inputName)

heroPertama = heroDota("dilabedil", 100, 78, 80)
print(heroDota.jumlah)
heroKedua = heroDota("cacamarica", 150, 67, 20)
print(heroDota.jumlah)
heroKetiga = heroDota("abdurh", 100, 75, 78)
print(heroDota.jumlah)
