class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        #self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property #decorator
    def armor(self):
        pass

    @armor.getter #decorator   
    def armor(self):
        return self.__armor

    @armor.setter #decorator
    def armor(self, input):
        self.__armor = input

    @armor.deleter #decorator
    def armor(self):
        print('armor di delete')
        self.__armor = None

Axe = Hero('axe', '100', '60')
print('merubah info')
print(Axe.info)
Axe.name = "mirana"
print(Axe.info)

print('getter and setter untuk __armor:')
print(Axe.armor)
Axe.armor = 10
print(Axe.armor)

print('delete armor')
del Axe.armor
print(Axe.__dict__)

#ENCAPSULASI DENGAN PYTHON MURNI BUKAN OOP