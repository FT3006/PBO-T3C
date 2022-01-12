class Hero:
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


class Hero_Mage(Hero):
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


class Hero_Tank(Hero):
	def __init__(self,name):
		super().__init__(name,200)


koeni = Hero_Mage('koeni')
surti = Hero_Tank('surti')

koeni.showInfo()
surti.showInfo()