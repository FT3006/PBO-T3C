class Hero: #template
	#class variabel
	jumlah = 0

	def __init__(self,inputName,inputHealth,inputPower,inputArmor):
		# instance variabel
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah += 1
		print("membuat Hero dengan nama " + inputName)


hero1 = Hero("Spiderman",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Ironman",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("Hulk",1000, 100, 0)
print(Hero.jumlah)