class Hero:

    # Private Class Variabel
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # Method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah2():
        return Hero.__jumlah

    # Method Static (decorator) menempel ke object dan class
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah

    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah

zeus = Hero("Zeus")
print(Hero.getjumlah2())
kratos = Hero("Kratos")
print(zeus.getjumlah2())
athena = Hero("Athena")
print(Hero.getjumlah3())