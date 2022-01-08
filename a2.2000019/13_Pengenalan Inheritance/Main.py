class Hero:

	def __init__(self,name,health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero):
	pass

class Hero_strength(Hero):
	pass

kaja = Hero('kaja',100)
diggie = Hero_intelligent('diggie',50)
mona = Hero_strength('mona',200)

print(kaja.name)
print(diggie.name)
print(mona.name)