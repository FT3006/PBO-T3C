class Hero :
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

zilong = Hero("zilong", 100)

print(zilong.__dict__)
#print(zilong.__private)
#zilong.__private = "testing"
#print(zilong._protected)
#zilong._protected = "testing"
print(zilong.__dict__)
#print(zilong.__private)
#print(zilong._protected)
print(Hero.__privateJumlah) 