class heroDota:#template
    #class variable
     jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
   
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
