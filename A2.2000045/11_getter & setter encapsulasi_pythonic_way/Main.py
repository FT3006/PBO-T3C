class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

#self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delet')
        self.__armor = None

mage = Hero('mage',100,10)

print('merubah info')
print(mage.info)
mage.name = 'Lylia'
print(mage.info)

print('getter dan setter untuk __armor:')
print(mage.armor)
mage.armor = 50
print(mage.armor)

print('delet armor')
del mage.armor
print(mage.__dict__) 