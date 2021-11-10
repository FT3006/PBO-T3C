class Hero:

    # class variabel
    jumlah = 0 
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variabel instance private
        self.__private = "private"
        # variable instance protected
        self._protected = "protected"

    

caka = Hero("caka",100)

print(caka.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)
