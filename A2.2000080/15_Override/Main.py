class hero_Dota2:
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


class hero_intelligent(hero_Dota2):
	def __init__(self,name):
		super().__init__(name,100)

	# override
	def showInfo(self):
		print("showInfo di subclass hero_intelligent")
		print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
		    self.name,
		    self.health
			)
		)


class hero_ability(hero_Dota2):
	def __init__(self,name):
		super().__init__(name,200)

    # override
	def showInfo(self):
		print("showInfo di subclass hero_ability")
		print("{} \n\tTipe: ability, \n\thealth: {}".format(
			self.name,
			self.health
			)
		)

Io = hero_intelligent('Io')
Medusa = hero_ability('Medusa')

Io.showInfo()
Medusa.showInfo()