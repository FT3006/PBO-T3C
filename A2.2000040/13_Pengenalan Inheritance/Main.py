class Hero:

   def __init__(self,name,health) :
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

lingling = Hero('lingling',100)
sardun = Hero_intelligent('sardun',50)
koeni = Hero_strength('koeni',200)

print(lingling.name)
print(sardun.name)
print(koeni.name)