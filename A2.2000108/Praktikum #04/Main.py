class heroOnepiece:

    jumlah = 0

    def _init_(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroOnepiece.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

heroPertama = heroOnepiece("Lufi", 100, 78, 80)
print(heroOnepiece.jumlah)
heroKedua = heroOnepiece("Zoro", 100, 67, 20)
print(heroOnepiece.jumlah)
heroKetiga = heroOnepiece("Sanji", 100, 79, 82)
print(heroOnepiece.jumlah)