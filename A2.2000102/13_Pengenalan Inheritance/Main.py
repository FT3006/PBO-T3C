class Hero:

   def __init__(self,name,health) :
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

Kala = Hero('Kala',100)
Caka = Hero_intelligent('Caka',50)
Reg = Hero_strength('Reg',200)

print(Kala.name)
print(Caka.name)
print(Reg.name)