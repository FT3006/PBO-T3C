class Hero :

  #private class variabel
  __jumlah = 0;

  def __init__(self, name) :
    self.__name = name
    Hero.__jumlah += 1

  #method ini hanya berlaku untuk objek
  def getJumlah(self) :
    return Hero.__jumlah

  #method ini hanya berlaku untuk class
  def getJumlah1() :
    return Hero.__jumlah

  #method static (decorator) nempel ke objek dan class
  @staticmethod
  def getJumlah2() :
    return Hero.__jumlah

  @classmethod 
  def getJumlah3(cls) :
    return cls.__jumlah

lingling = Hero('lingling')
print(Hero.getJumlah2())
sarbud = Hero('sarbud')
print(Hero.getJumlah2())
koeni = Hero('koeni')
print(Hero.getJumlah3())