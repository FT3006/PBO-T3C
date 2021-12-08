class Hero:

    def __init__(self,name,health,armor):
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
        print("Armor yang di delete")
        self.__armor = None

zeus = Hero("Zeus",100,10)

print("Merubah info")
print(zeus.info)
zeus.name = "Josep"
print(zeus.info)

print("Getter dan Setter untuk __armor : ")
print(zeus.armor)
zeus.armor = 50
print(zeus.armor)

print("Delete Armor")
del zeus.armor
print(zeus.__dict__)