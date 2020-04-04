class MhsTIF():
    def __init__(self, nama, nim, kota, uang, Next=None):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang
        self.Next = None
    def __str__(self):
        return ("\nNama\t: "+ self.nama +\
                "\nNIM\t: "+ str(self.nim) +\
                "\nKota\t: "+ self.kota +\
                "\nUang\t: RP."+ str(self.uang))

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)


db = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
print(db[0])
