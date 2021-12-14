class HeroMobileLegends :

  #private class variabel
  __jumlah = 0;

  def __init__(self, name) :
    self.__name = name
    HeroMobileLegends.__jumlah += 1

  #method ini hanya berlaku untuk objek
  def getJumlah(self) :
    return HeroMobileLegends.__jumlah

  #method ini hanya berlaku untuk class
  def getJumlah1() :
    return HeroMobileLegends.__jumlah

  #method static (decorator) nempel ke objek dan class
  @staticmethod
  def getJumlah2() :
    return HeroMobileLegends.__jumlah

  @classmethod 
  def getJumlah3(cls) :
    return cls.__jumlah

Martis = HeroMobileLegends('Martis')
print(HeroMobileLegends.getJumlah2())
Yuzhong = HeroMobileLegends('Yuzhong')
print(Martis.getJumlah2())
Freya = HeroMobileLegends('Freya')
print(HeroMobileLegends.getJumlah3())