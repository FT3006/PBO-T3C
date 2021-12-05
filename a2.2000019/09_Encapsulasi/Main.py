class Hero:

    def __init__(self,name,healt,attackPower):
        self.__name = name
        self.__healt = healt
        self.__attPower = attackPower

    #getter
    def getName(self):
        return self.__name

    def getHealt(self):
        return self.__healt

    #setter
    def diserang(self, serangPower):
        self.__healt -= serangPower

    def setAttPower(self, nilaibaru):
        self.__attPower -= nilaibaru


#awal dari game
Phylax = Hero("Phylax", 50, 5)

#game berjalan
print(Phylax.getName())
print(Phylax.getHealt())
Phylax.diserang(5)
print(Phylax.getHealt())