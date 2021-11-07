class heroleagueoflegends: #template
    #class variable
    
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroleagueoflegends.jumlah += 1
        print("membuat hero dengan nama " + inputName)

heroPertama = heroleagueoflegends("Ahri", 100, 78, 70)
print(heroleagueoflegends.jumlah)
heroKedua = heroleagueoflegends("Alistar", 150, 87, 30)
print(heroleagueoflegends.jumlah)
heroKetiga = heroleagueoflegends("Braum", 200, 95, 68)
print(heroleagueoflegends.jumlah)
