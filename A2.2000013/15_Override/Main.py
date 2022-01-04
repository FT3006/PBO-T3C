class HeroMobileLegends:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("showInfo di class Hero")
		print("{} health: {}".format(
			self.name,
			self.health
			)
		)


class HeroMobileLegends_Mage(HeroMobileLegends):
	def __init__(self,name):
		super().__init__(name,100)

	# override
	def showInfo(self):
		print("showInfo di subclass Hero_Mage")
		print("{} \n\tTipe: Mage, \n\thealth: {}".format(
			self.name,
			self.health
			)
		)


class HeroMobileLegends_Tank(HeroMobileLegends):
	def __init__(self,name):
		super().__init__(name,200)


Selena = HeroMobileLegends_Mage('Selena')
Atlas = HeroMobileLegends_Tank('Atlas')

Selena.showInfo()
Atlas.showInfo()