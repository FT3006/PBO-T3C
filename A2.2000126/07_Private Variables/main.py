class hero:
    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

        # variable instance private
        self.__private = "private"
        self._protected = "protected"

ripan = hero("ripan",100)

print(ripan.__dict__)
print(hero.__dict__)
print(hero.__privateJumlah)