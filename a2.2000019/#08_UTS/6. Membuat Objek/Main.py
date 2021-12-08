class Kendaraan:
    bahan_bakar = "Bensin"

    def __init__(self, kendaraan):
        self.kendaraan = kendaraan
        print("Bahan Bakar " + self.kendaraan + " Adalah")

mobil = Kendaraan ("Mobil")

print(mobil.bahan_bakar) 