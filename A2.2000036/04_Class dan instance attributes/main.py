class heroML:

    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroML.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

heroPertama = heroML("zilong", 100, 78, 80)
print(heroML.jumlah)
heroKedua = heroML("layla", 100, 67, 20)
print(heroML.jumlah)
heroKetiga = heroML("miya", 100, 79, 82)
print(heroML.jumlah)