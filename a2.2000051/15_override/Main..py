class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showinfo(self):
        print("showinfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )


class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    # override
    def showinfo(self):
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
             )
        )



class Hero_strenght(Hero):
    def __init__(self,name):
        super().__init__(name,200)


hadi = Hero_intelligent('hadi')
kinan = Hero_strenght('kinan')

hadi.showinfo()



