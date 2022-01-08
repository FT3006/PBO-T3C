class HeroMobileLegends:
  def __init__(self, name, health):
    self.name = name 
    self.health = health

  def showInfo(self):
    print('Health {} = {}'.format(self.name , self.health))

class HeroTank(HeroMobileLegends):
  def __init__(self,name):
    #self.name = name
    #self.health = 200
    #HeroMobileLegends.__init__(self, name, 200)
    super().__init__(name, 200)
    super().showInfo()

class HeroFighter(HeroMobileLegends):
  def __init__(self,name):
    #self.name = name
    #self.health = 200
    #HeroMobileLegends.__init__(self, name, 100)
    super().__init__(name, 100)
    super().showInfo()

class HeroAssassin(HeroMobileLegends):
  def __init__(self,name):
    #self.name = name
    #self.health = 100
    #HeroMobileLegends.__init__(self, name, 80)
    super().__init__(name, 80)
    super().showInfo()

class HeroMage(HeroMobileLegends):
  def __init__(self,name):
    #self.name = name
    #self.health = 200
    #HeroMobileLegends.__init__(self, name, 60)
    super().__init__(name, 60)
    super().showInfo()

Uranus = HeroTank('Uranus')
Masha = HeroFighter('Masha') 
Ling = HeroAssassin('Ling')
Kagura = HeroMage('Kagura')

#print(Uranus.name , '' , Uranus.health)
#print(Roger.name , '' , Roger.health)
#print(Lancelot.name , '' , Lancelot.health)
#print(Nana.name , '' , Nana.health)
