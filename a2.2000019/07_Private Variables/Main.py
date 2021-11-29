class Hero:

    # variable class
    jumlah = 0
    __privateJumlah = 0 

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # private instance variable
        self.__private = "private"
        # protected instance variable
        self._protected = "protected"

phylax = Hero("phylax", 100)

print(phylax.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)