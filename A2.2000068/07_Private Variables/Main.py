class HeroMobileLegends :
  #template
  jumlah = 0
  __privateJumlah = 0

  def __init__(self, name, health):
    self.name = name
    self.health = health

    #Variabel instance Private
    self.__private = "private"

    #Variabel instance Protected
    self._protected = "protected"

Kufra = HeroMobileLegends("Kufra", 100)

print(Kufra.__dict__)
#print(Kufra.__private)
#Kufra.__private = "testing"
#print(Kufra._protected)
#Kufra._protected = "testing"
print(Kufra.__dict__)
#print(Kufra.__private)
#print(Kufra._protected)
print(HeroMobileLegends.__privateJumlah)