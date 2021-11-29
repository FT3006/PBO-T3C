class heroGenshinimpact:
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroGenshinimpact.jumlah += 1
        print("Membuat hero dengan nama " + inputName)

heroPertama = heroGenshinimpact("Kazuha", 100, 78, 70)
print(heroGenshinimpact.jumlah)
heroKedua = heroGenshinimpact("Yoimiya", 150, 87, 30)
print(heroGenshinimpact.jumlah)
heroKetiga = heroGenshinimpact("Mona", 200, 95, 68)
print(heroGenshinimpact.jumlah)