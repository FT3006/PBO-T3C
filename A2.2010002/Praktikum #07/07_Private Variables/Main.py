class superCar:

    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,cc):
        self.name = name
        self.cc = cc

    # variable instance private
    self.__private = "private"
    # variable instance protected
    self._protected = "protected"


lamborgini = superCar("lamborgini",1000)

print(lamborgini.__dict__)
print(superCar.__dict__)
print(superCar.__privateJumlah)