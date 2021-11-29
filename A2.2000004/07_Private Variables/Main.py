class Hero:

    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        #variabel instance private
        self.__private = "private"
        #variabel instance protected
        self._protected = "protected"


Gatotkaca = Hero("Gatotkaca",100)

print(Gatotkaca.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)