class Hero:

    #private class variabel
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

Lunox = Hero('Lunox')
print(Hero.getJumlah2())
Nana = Hero('Nana')
print(Lunox.getJumlah2())
Miya = Hero('Miya')
print(Hero.getJumlah3()) 