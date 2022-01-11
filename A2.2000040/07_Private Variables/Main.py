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

koeni = Hero("koeni", 100)

print(koeni.__dict__)
#print(Koeni.__private)
#Koeni.__private = "testing"
#print(koeni._protected)
#Koeni._protected = "testing"
print(koeni.__dict__)
#print(Koeni.__private)
#print(Koeni._protected)
print(Hero.__privateJumlah)