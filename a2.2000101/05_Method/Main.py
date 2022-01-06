class heroleagueoflegends: #template
    #class variable
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroleagueoflegends.jumlah += 1
# void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(" Nama Hero Adalah " + self.name)

# method dengana rgumen, tanpa return
    def armorUp(self, up):
        self.armor +=up

# void function, method tanpa return, tanpa argumen
    def getArmor(self):
        return self.armor

heroPertama = heroleagueoflegends("Ahri", 100, 78, 70)
heroPertama.siapa()
heroPertama.armorUp(70)
print(heroPertama.getArmor())
