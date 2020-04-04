#Author : Ridwan Renaldi (L200160026)
#Kelas : B
#Python 3.6



#=====[No 1]=====
class Pesan ():
    def __init__(self, sebuahString):
        self.teks = sebuahString

    def apakahTerkandung (self, terserah):
        if terserah in self.teks:
            print(True)
        else:
            print(False)

    def hitungKonsonan(self):
        vokal = ['a', 'i', 'u', 'e', 'o']
        hurufKonsonan = 0
        
        for x in self.teks.lower():
            if x in vokal:
                pass
            else:
                hurufKonsonan += 1
        print(hurufKonsonan)

    def hitungVokal(self):
        vokal = ['a', 'i', 'u', 'e', 'o']
        hurufVokal = 0

        for o in self.teks.lower():
            if o in vokal:
                hurufVokal += 1
            else:
                pass
        print(hurufVokal)

##ASD = Pesan("Hello World")
##ASD.apakahTerkandung("Hello")
##ASD.hitungKonsonan()
##ASD.hitungVokal()



class Manusia(object):
	""" Class Manusia dengan inisial nama"""
	keadaan="lapar"	
	def __init__(self, nama):
		self.nama=nama

	def ucapkanSalam(self):
		print("Salam, Namaku ", self.nama)

	def makan(self, s):
		print("Saya baru saja makan ", self.s)
		keadaan="kenyang"

	def olahraga(self, k):
		print("Saya baru saja latihan ", k)
		keadaan="lapar"

	def mengalikanDenganDua(self, n):
		return n*2


#=====[No 2]=====
class Mahasiswa():
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        s = str(self.nama) + ", NIM " + str(self.NIM) \
	+  ", Tinggal di "+ str(self.kotaTinggal) \
	+  ", Uang Saku Rp " +str(self.uangSaku) \
	+ " tiap bulannya"
        return s
    
    def ambilNama(self):
        return self.nama

    def ambilNim(self):
        return self.NIM
    
    def ambilKotaTinggal(self):
        return(self.kotaTinggal)
    
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    
    def ambilUangSaku(self):
        return(self.uangSaku)
    
    def tambahUangSaku(self, uangTambah):
        self.uangSaku += uangTambah

    def makan(self, s):
        """ Metode ini Menutupi metode makannya class manusia"""
        print("Saya baru saja makan ", s, " Sambil Belajar")
        self.keadaan='kenyang'

##ASD = Mahasiswa("Ridwan", "L200160026", "Solo", 12000)
##print(ASD.ambilKotaTinggal())
##ASD.perbaruiKotaTinggal("Surakarta")
##print(ASD.ambilKotaTinggal())
##print(ASD.ambilUangSaku())
##ASD.tambahUangSaku(3500)
##print(ASD.ambilUangSaku())

#=====[No 3]=====

def tampilkan(dt):
    print("=========================")
    print("Data Mahasiswa")
    print("=========================")
    print("Nama\t\t:", dt.ambilNama())
    print("NIM\t\t:", dt.ambilNim())
    print("Kota Tinggal\t:", dt.ambilKotaTinggal())
    print("Uang Saku\t:", dt.ambilUangSaku())
    print("=========================")

def inputData():
    print("=========================")
    print("Input Data Mahasiswa")
    print("=========================")
    NAMA = str(input("Nama\t\t:"))
    NIM  = str(input("NIM\t\t:"))
    KOTA = str(input("Kota\t\t:"))
    UANG = str(input("Uang Saku\t:"))
    DATA = Mahasiswa(NAMA, NIM, KOTA, UANG)
    print("=========================\n")
    return DATA

def Menu():
    print("\n=========================")
    print("Menu Aplikasi Mahasiswa")
    print("=========================")
    print("[1] Input Data")
    print("[2] Tampilkan Data")
    print("[3] Edit  Data")
    print("[4] Delete Data")
    print("[0] Keluar")
    print("=========================")


keluar = False
db = []
while keluar is not True:
    Menu()
    pilihan = input("Pilih Menu : ")
    if pilihan.isnumeric() == True:
        pilihan = int(pilihan)
    print("\n")
    if pilihan is 1:
        db.append(inputData())
        
    elif pilihan is 2:
        if len(db) == 0:
            print("Tidak Ada Data")
        else :
            for i in range(len(db)):
                print("["+str(i)+"] NIM : ",db[i].ambilNim())
            plh = int(input("Pilih Data : "))
            if plh in range(len(db)):
                tampilkan(db[plh])
            else:
                print("Salah input")
            
    elif pilihan is 3:
        if len(db) == 0:
            print("Tidak Ada Data")
        else:
            for i in range(len(db)):
                print("["+str(i)+"] NIM : ",db[i].ambilNim())
            plh = int(input("Pilih Data : "))
            if plh in range(len(db)):
                edit = inputData()
                db[plh] = edit
            else:
                print("Salah input")
        
    elif pilihan is 4:
        if len(db) == 0:
            print("Tidak Ada Data")
        else:
            for i in range(len(db)):
                print("["+str(i)+"] NIM : ",db[i].ambilNim())
            plh = int(input("Pilih Data : "))
            if plh in range(len(db)):
                del db[plh]
                print("Data Terhapus...")
            else:
                print("Salah input")
            
    elif pilihan is 0:
        print("Keluar...")
        keluar = True

    else:
        print("Salah input")
    
