class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
     self.name = inputName 
     self.health = inputHealth
     self.power = inputPower
     self.armor = inputArmor 

hero1 =Hero("SUGIH",100, 10, 4)
hero2 =Hero("DEDE",100, 15, 1)
hero3 =Hero("IVAN",1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)