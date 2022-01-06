class Hero:

	def __init__(self,name,health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero):
	pass

class Hero_strength(Hero):
	pass

hadi = Hero('hadi',100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(hadi.name)
print(techies.name)
print(axe.name)
