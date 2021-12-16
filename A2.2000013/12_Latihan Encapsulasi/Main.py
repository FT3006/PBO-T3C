class HeroMobileLegends: 

	#private class variabel
	__jumlah = 0

	def __init__(self,name,health,attPower,armor):
		self.__name = name
		self.__healthStandar = health
		self.__attPowerStandar = attPower
		self.__armorStandar = armor
		self.__level = 1
		self.__exp = 0

		self._healthMax = self.healthStandar * self._level
		self._attPower = self.attPowerStandar * self._level
		self._armor = self.armorStandar * self._level

		self._health = self._healthMax

		HeroMobileLegends.__jumlah += 1

	@property
	def info(self):
		return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self._name,self.level,self.health,self.healthMax,self.attPower,self._armor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self,addExp):
		self.__exp += addExp
		if (self.__exp >= 100):
			print(self.__name, 'level up')
			self.__level += 1
			self.__exp -= 100

			self._healthMax = self.healthStandar * self._level
			self._attPower = self.attPowerStandar * self._level
			self._armor = self.armorStandar * self._level

	def attack(self,musuh):
		self.gainExp = 50

Harits = HeroMobileLegends('Harits', 100, 5, 10)
Harley = HeroMobileLegends('Harley', 100, 5, 10)
print(Harits.info)

Harits.attack(Harley)
Harits.attack(Harley)
Harits.attack(Harley)

print(Harits.info)