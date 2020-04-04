#AUTHOR : RIDWAN RENALDI (L200160026)
#Kelas  : B
#Python 3.6

#====================================[NO 1]=====================================
def cekMatrix(mtrx):
    jmlh = len(mtrx)
    hasil = ""
    for x in mtrx:
        if hasil == "False":
            break
        else:
            if len(x) == jmlh:
                for i in x:
                    if type(i) == int:
                        hasil = "True"
                    else:
                        hasil = "False"
                        break
            else:
                hasil = "False"
                break
    return hasil
    #print (hasil)

asd = [[1,2,3],[4,5,6],[7,8,9]]
print (cekMatrix(asd))


def Ukuran(mtrx):
    print ("Ukuran matrix = "+str(len(mtrx))+" x "+str(len(mtrx[0])))


def Penjumlahan(mtrxA,mtrxB):
    if cekMatrix(mtrxA) == cekMatrix(mtrxB):
        data2 = []
        for x in range(len(mtrxA)):
            data1 = []
            for i in range(len(mtrxB)):
                hasil = mtrxA[x][i] + mtrxB[x][i]
                data1.append(hasil)
            data2.append(data1)
        print (data2)
    else:
        print ("Matrix tidak sama")
            
def Perkalian(mtrxA,mtrxB):
    hasil = []
    for n in range(len(mtrxA)):
        row = []
        for x in range(len(mtrxB[0])):
            total = 0
            for y in range(len(mtrxA[n])):
                total += (mtrxA[n][y] * mtrxB[y][x])
            row.append(total)
        hasil.append(row)
    print (hasil)

"Contoh matrix dapat dilihat disini : http://www.edutafsi.com/2014/11/kumpulan-soal-dan-pembahasan-perkalian.html"
#data1 = [[2,3],[4,4]]
#data2 = [[4,3],[-4,6]]

#data1 = [[2,1,2],[1,2,1]]
#data2 = [[2,1,4],[1,2,3],[2,2,1]]

#data1 = [[2],[4],[3]]
#data2 = [[1,-2,4]]

#data1 = [[2,4,-2],[3,2,1],[-2,2,2],[1,3,4]]
#data2 = [[3,2],[2,3],[3,2]]

"Contoh matrix dapat dilihat disini : https://penma2b.id/2017/03/05/perkalian-matriks-trik-pensil/"
#data1 = [[1,2],[3,4]]
#data2 = [[5,6,7],[8,9,10]]

#data1 = [[1],[2]]
#data2 = [[3,4,5,6,7]]

#data1 = [[1,2,3],[4,5,6],[7,8,9]]
#data2 = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
#Perkalian(data1,data2)


def Determinan(mtrx):
    if cekMatrix(mtrx) == "True":
        if len(mtrx) == 2:
            nilai = (mtrx[0][0] * mtrx[1][1]) - (mtrx[0][1]*mtrx[1][0])
            print (nilai)
        else:
            bil1 = [x for x in range(len(mtrx))]
            jumlah1 = 0
            for i in range(len(mtrx)):
                total1 = 1
                for x in range(len(mtrx)):
                    total1 *= mtrx[x][bil1[x]]
                bil1 += [bil1.pop(0)] #Menggeser list ke kiri
                jumlah1 += total1

        
            bil2 = [x for x in range(len(mtrx))]
            bil2.reverse()
            jumlah2 = 0
            for i in range(len(mtrx)):
                total2 = 1
                for x in range(len(mtrx)):
                    total2 *= mtrx[x][bil2[x]]
                bil2.insert(0, bil2.pop())#Menggeser list ke kanan
                jumlah2 += total2

            hasil = jumlah1-jumlah2
            print (hasil)
    else:
        print ("Matrix harus bujursangkar")

#A = [[1,2,3],[2,1,4],[3,1,2]]
#B = [[-2,0,-5],[1,3,0],[-1,4,-8]]
#C = [[-2,4,-5],[1,3,-7],[-1,4,-8]]
#D = [[2,3,4],[5,4,3],[7,0,1]]
#E = [[1,2,3,4],[8,7,6,5],[9,-1,-2,-3],[-4,-5,-5,-4]]
#Determinan(E)

#====================================[NO 2]=====================================

def buatNol(x,y=1):
    mtrx = [[0 for x in range(x)] for i in range(y)]
    print (mtrx)


def buatIdentitas(x,y=1):
    mtrx = [[1 if j==i else 0 for j in range(x)] for i in range(y)]
    print (mtrx)

#buatIdentitas(3,3)
#buatNol(3,3)
#====================================[NO 3]=====================================

class Node():
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


def cetak(head):
    curr = head
    while curr is not None:
        print (curr.data)
        curr = curr.nextNode

def cari(head, yang_dicari):
    curr = head
    while curr is not None:
        if curr.data == yang_dicari:
            print ("Data ditemukan!")
        else:
            print ("Check data!")
        curr = curr.nextNode
        
def tambahDepan(head):
    newNode = Node(1)
    newNode.nextNode = head
    head = newNode
    return head

def tambahAkhir(head):
    curr = head
    while curr is not None:
        if curr.nextNode == None:
            newNode = Node(25)
            curr.nextNode = newNode
            return curr
        else:
            #print(curr.data)
            pass
        curr = curr.nextNode
    return curr

def tambah(head,posisi):
    newNode = Node(8)
    newNode.nextNode = posisi.nextNode
    posisi.nextNode = newNode

    head.head = posisi
    return head
    
def hapus(head, posisi):
    curr = head
    while curr is not None:
        if curr.nextNode.data == posisi:
            curr.nextNode = curr.nextNode.nextNode
            return curr
        else:
            pass
        curr = curr.nextNode
    return curr

a = Node(3)
b = Node(7)
c = Node(11)
d = Node(13)

a.nextNode = b
b.nextNode = c
c.nextNode = d


#Menjalankan fungsi cari
print("===Mencari Data===")
cari(a,11)

print("\n\n")
#Menambah simpul di depan
print ("===Sebelum Ditambah di Depan===")
cetak(a)
tmbhn = tambahDepan(a)
print ("===Sesudah Ditambah di Depan===")
cetak(tmbhn)

print("\n\n")
#Menambah simpul di akhir
print ("===Sebelum Ditambah di Akhir===")
cetak(b)
tambahAkhir(b)
print ("===Sesudah Ditambah di Akhir===")
cetak(b)

print("\n\n")
#Menyisipkan simpul
print("===Sebelum di sisipkan===")
cetak(a)
tmbhn = tambah(a,b)
print("===Sesudah di sisipkan===")
cetak(tmbhn)

print("\n\n")
#Menghapus posisi
print("===Sebelum Dihapus===")
cetak(b)
hapus(a,13)
print("===Sesudah Dihapus===")
cetak(b)

print("\n\n")

#====================================[NO 4]=====================================
class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

def mencetak(head):
    curr = head
    while curr is not None:
        print(curr.Data)
        if curr.Next == None:
            curr = curr
            break
        else:
            curr = curr.Next
    print ("\n")
    while curr is not None:
        print(curr.Data)
        curr = curr.Prev

def simpulAwal(head):
    newNode = doubly_linked(25)
    newNode.Next = head
    head.Prev = newNode
    head = newNode
    return head

def simpulAkhir(head):
    curr = head
    while curr is not None:
        if curr.Next == None:
            newNode = doubly_linked(365)
            
            curr.Next = newNode
            newNode.Prev = curr
            return curr
        else:
            #print(curr.data)
            pass
        curr = curr.Next
    return curr

s1 = doubly_linked(1)
s2 = doubly_linked(2)
s3 = doubly_linked(3)
s4 = doubly_linked(4)


s1.Next = s2
s1.Prev = None
s2.Next = s3
s2.Prev = s1
s3.Next = s4
s3.Prev = s2
s4.Next = None
s4.Prev = s3

print("=======[NO 4.a]=========")
mencetak(s1)

print("\n=======[NO 4.b]=========")
s1 = simpulAwal(s1)
mencetak(s1)

print("\n=======[NO 4.c]=========")
simpulAkhir(s1)
mencetak(s1)
