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

spiderman = Hero("spiderman", 100)

print(spiderman.__dict__)
#print(spiderman.__private)
#spiderman.__private = "testing"
#print(spiderman._protected)
#spiderman._protected = "testing"
print(spiderman.__dict__)
#print(spiderman.__private)
#print(spiderman._protected)
print(Hero.__privateJumlah) 
