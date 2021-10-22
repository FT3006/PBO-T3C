class HunterXHunter: # template
    # class variable
    jumlah = 0

    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        HunterXHunter.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

hero1 = HunterXHunter("Gon", 100, 20, 3)
print(HunterXHunter.jumlah)
hero2 = HunterXHunter("Killua", 100, 13, 5)
print(HunterXHunter.jumlah)
hero3 = HunterXHunter("Kurapika", 100, 20, 7)
print(HunterXHunter.jumlah)
hero4 = HunterXHunter("Leorio", 100, 7, 18)
print(HunterXHunter.jumlah)
