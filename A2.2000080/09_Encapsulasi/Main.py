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
tinker = Hero("tinker", 100, 10)

#game berjalan
print(tinker.getName())
print(tinker.getHealt())
tinker.diserang(10)
print(tinker.getHealt())