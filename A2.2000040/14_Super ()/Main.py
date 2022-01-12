class Hero:
  def __init__(self, name, health):
    self.name = name 
    self.health = health

  def showInfo(self):
    print('Health {} = {}'.format(self.name , self.health))

class HeroTank(Hero):
  def __init__(self,name):
    #self.name = name
    #self.health = 200
    #Hero.__init__(self, name, 200)
    super().__init__(name, 200)
    super().showInfo()

class HeroFighter(Hero):
  def __init__(self,name):
    #self.name = name
    #self.health = 200
    #Hero.__init__(self, name, 100)
    super().__init__(name, 100)
    super().showInfo()

class HeroAssassin(Hero):
  def __init__(self,name):
    #self.name = name
    #self.health = 100
    #Hero.__init__(self, name, 65)
    super().__init__(name, 65)
    super().showInfo()

class HeroMage(Hero):
  def __init__(self,name):
    #self.name = name
    #self.health = 200
    #Hero.__init__(self, name, 60)
    super().__init__(name, 60)
    super().showInfo()

lingling = HeroTank('lingling')
sardun = HeroFighter('sardun') 
koeni = HeroAssassin('koeni')
surti = HeroMage('surti')

#print(lingling.name , '' , lingling.health)
#print(sardun.name , '' , sardun.health)
#print(koeni.name , '' , koeni.health)
#print(surti.name , '' , surti.health)
