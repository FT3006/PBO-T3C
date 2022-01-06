class Kendaraan:
  bahan_bakar = "Bensin"

  def __init__(self, kendaraan):
    self.kendaraan = kendaraan

mobil = Kendaraan ("Mobil")

print("Bahan Bakar mobil adalah " + mobil.bahan_bakar)