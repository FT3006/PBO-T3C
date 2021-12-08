class Kendaraan:
    bahan_bakar = "Bensin"

    def __init__(self, Kendaraan):
        self.Kendaraan = Kendaraan 
        print("Bahan Bakar " + self.Kendaraan + " Adalah")

mobil = Kendaraan ("Mobil")

print(mobil.bahan_bakar)