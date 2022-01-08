class Hero:

   def __init__(self,name,health) :
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

Alu = Hero('Alu',100)
Yve = Hero_intelligent('Yve',50)
Nana = Hero_strength('Nana',200)

print(Alu.name)
print(Yve.name)
print(Nana.name)