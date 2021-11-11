class hero: # template
    pass

hero1 = hero() # object / instance
hero2 = hero()
hero3 = hero();

hero1.name = "zilong"
hero1.health = 100

hero2.name = "miya"
hero2.health = 50

hero3.name = "nana"
hero3.health = 40

print(hero1)
print(hero1.__dict__)

print(hero2)
print(hero2.__dict__)

print(hero3)
print(hero3.__dict__)
