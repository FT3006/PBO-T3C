class heroDota:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    jumlah = 0
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroDota.jumlah += 1

# void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(" Namaku Adalah " + self.name)

# method dengana rgumen, tanpa return
    def power(self, up):
        self.power +=up

# void function, method tanpa return, tanpa argumen
    def getPower(self):
        return self.power


heroPertama = heroDota("dilabedil", 100, 78, 80)
heroPertama.apa()
heroPertama.powerUp(78)
print(heroPertama.getPower())

