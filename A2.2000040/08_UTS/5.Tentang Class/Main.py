class Kendaraan:
  bahan_bakar = "pertalite"

  def __init__(self, kendaraan):
    self.kendaraan = kendaraan

mobil = Kendaraan ("Motor")

print("Bahan bakar motor adalah " + mobil.bahan_bakar)