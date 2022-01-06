class hero:

    def __init__(self, name, HP, damage, armor):
        self.name = name
        self.HP = HP
        self.damage = damage
        self.armor = armor
    
    def attack(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.damage)

    def diserang(self, lawan, damage_lawan):
        print(self.name + " diserang " + lawan.name)
        damage_diterima = damage_lawan/self.armor
        print("deal damage : " +  str(damage_diterima))
        self.HP -= damage_diterima
        print(" HP " + self.name + " tersisa " + str(self.HP))

ripan = hero("ripan",100, 75, 10)
wandi = hero("wandi",100, 50, 15)

wandi.attack(ripan)
print("\n")
ripan.attack(wandi)
print("\n")
wandi.attack(ripan)
print("\n")
ripan.attack(wandi)
print("\n")
wandi.attack(ripan)
print("\n")
ripan.attack(wandi)
print("\n")
wandi.attack(ripan)
print("\n")
ripan.attack(wandi)
print("\n")
wandi.attack(ripan)
print("\n")
ripan.attack(wandi)
print("\n")

