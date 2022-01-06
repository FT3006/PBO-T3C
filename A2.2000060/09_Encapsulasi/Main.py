class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # Getter

    def getname(self):
        return self.__name

    def gethealth(self):
        return self.__health
    
    # Setter

    def diserang(self,hitPower):
        self.__health -= hitPower
    
    def setAttPower(self,nilaibaru):
        self.__attackPower = nilaibaru

# Awal dari Game
zeus = Hero("Zeus",105,10)

# Game Berjalan

print(zeus.getname())
print(zeus.gethealth())
zeus.diserang(15)
print(zeus.gethealth())