class Hero:

    # class variable
    jumlah = 0
    __privateJumlah = 0

def __(self,name,health):
    self.name = name
    self.health = health

    # variable instace private
    self.__private ="private"
    # variable instance protected
    self.__protected ="protected"



papaw = Hero("papaw",100)

print(papaw.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)