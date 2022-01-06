class jawaraSumedang:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

jawaraPertama = jawaraSumedang("arincodet", 100, 78, 80)
jawaraKedua   = jawaraSumedang("casadis", 100, 90, 20)
jawaraKetiga  = jawaraSumedang("abdurh", 150, 75, 78)

print(jawaraPertama.__dict__)
print(jawaraKedua.__dict__)
print(jawaraKetiga.__dict__)