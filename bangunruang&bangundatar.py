import modulbangunruang as mbr, modulbangundatar as mbd


print("~~~ BANGUN RUANG ~~~")
print(f"volum kubus dengan sisi 6 adalah {mbr.kubus(3)}")
print(f"volum balok adalah {mbr.balok(4,5,6)}")
print(f"volum prisma segitiga adalah {mbr.prisma(6,3,6)}")
print(f"Volum Tabung adalah {mbr.tabung(6,9)}")
print(f"Volum Kerucut adalah {mbr.kerucut(3,9)}")

print("~~~ BANGUN DATAR ~~~")
print(f"Luas Persegi adalah {mbd.persegi(8)} ")
print(f"Luas Persegi Panjang adalah {mbd.persegi_panjang(16,8)} ")
print(f"Luas Segitiga adalah {mbd.segitiga(9,6)} ")
print(f"Luas Lingkaran adalah {mbd.lingkaran(6)}")
print(f"Luas JajarGenjanng adalah {mbd.jajargenjang(6,8)} ")