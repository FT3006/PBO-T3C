class HunterXHunter: # template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = HunterXHunter("Gon", 100, 20, 2)
hero2 = HunterXHunter("Killua", 100, 13, 5)
hero3 = HunterXHunter("Kurapika", 100, 20, 7)
hero4 = HunterXHunter("Leorio", 100, 7, 18)

print(hero1.name)
print(hero2.health)
print(hero3.armor)
print(hero4.name)