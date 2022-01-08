class Hero:

	def __init__(self,name,health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero):
	pass

class Hero_strength(Hero):
	pass

kratos = Hero('Kratos',100)
hades = Hero_intelligent('Hades',50)
Zeus = Hero_strength('Zeus',200)

print(kratos.name)
print(hades.name)
print(Zeus.name)