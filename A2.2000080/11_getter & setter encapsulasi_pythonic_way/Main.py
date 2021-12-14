class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		#self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property
	def armor(self):
		pass

	@armor.getter
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self, input):
		self.__armor = input

	@armor.deleter
	def armor(self):
		print('armor di delet')
		self.__armor = None

Fighter = Hero('Fighter',100,10)

print('merubah info')
print(Fighter.info)
Fighter.name = 'Freya'
print(Fighter.info)

print('getter dan setter untuk __armor:')
print(Fighter.armor)
Fighter.armor = 50
print(Fighter.armor)

print('delete armor')
del Fighter.armor
print(Fighter.__dict__)