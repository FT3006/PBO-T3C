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

wadin = hero("wadin",1000, 750, 5)
kaguya = hero("kaguya",1000, 500, 10)

wadin.attack(kaguya)
print("\n")
kaguya.attack(wadin)
print("\n")
wadin.attack(kaguya)
print("\n")
kaguya.attack(wadin)
print("\n")
wadin.attack(kaguya)
print("\n")
kaguya.attack(wadin)
print("\n")
wadin.attack(kaguya)
print("\n")
kaguya.attack(wadin)
print("\n")
wadin.attack(kaguya)
print("\n")
kaguya.attack(wadin)