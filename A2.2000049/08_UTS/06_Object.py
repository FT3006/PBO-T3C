#Gadget
class Gadget(object):    
    sumber_energi = "listrik"   

hp = Gadget()
print('Sumber Energi Gadget : ' + str(hp.sumber_energi))

#Kendaraan
class Kendaraan(object):
    bahan_bakar = "bensin"

mobil = Kendaraan()
print('Bahan Bakar Mobil : ' + str(mobil.bahan_bakar))