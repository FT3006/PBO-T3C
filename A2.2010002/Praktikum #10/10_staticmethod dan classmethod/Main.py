class Hero:

    #private class variabel
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getjumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke objek dan class nya 
    @staticmethod 
    def getjumlah2():
        return Hero.__jumlah

    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah



kilua = Hero('kilua')
print(Hero.getjumlah1())
gon = Hero('gon')
print(gon.getjumlah2())
shinki = Hero('shinki')
print(shinki.getjumlah3())