class heroMl:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

heroPertama = heroMl("wadin", 100, 78, 80)
heroKedua = heroMl("ucup", 100, 67, 20)
heroKetiga = heroMl("abay", 100, 79, 82)
print(heroPertama.__dict__)
print(heroKedua.__dict__)
print(heroKetiga.__dict__)