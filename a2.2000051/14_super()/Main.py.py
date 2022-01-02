class Hero:
     def __init__(self,name,health):
        self.name = name
        self.health = health

     def showinfo(self):
         print ("{} dengan health: {}".format(self.name,self.health))

class Hero_intelligent(Hero):
     def __init__(self,name):
        #Hero.__init__(self,name, 100)
        super().__init__(name, 100)
        super().showinfo()
        
class Hero_strength(Hero):
     def __init__(self,name):
        super().__init__(name, 200)
        super().showinfo()

hadi= Hero_intelligent('hadi')
kinan = Hero_strength('kinan')

