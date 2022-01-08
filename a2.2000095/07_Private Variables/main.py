
 
class Hero:
 
    jumlah = 0
    __privateJumlah = 0
 
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__private = "private"
        self._protected = "protected" 
 
lina = Hero("GatotKaca",100)
 
print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah) 
