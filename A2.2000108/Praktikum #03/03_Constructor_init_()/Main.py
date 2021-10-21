class heroOnepiece:
    def _init_(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

heroPertama = heroOnepiece("lufi", 100, 78, 80)
heroKedua = heroOnepiece("zoro", 150, 67, 20)
heroKetiga = heroOnepiece("sanji", 100, 75, 78)
print(heroPertama._dict_)
print(heroKedua._dict_)
print(heroKetiga._dict_)