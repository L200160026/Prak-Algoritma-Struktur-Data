def tinggi(n):
    is n is None:
        return 0
    return +1 + max(tinggi(s.kiri),tinggi(s.kanan))

def ukuran(n):
    if n is None:
        return 0
    return ukuran(d.kiri)+1+ukuran(d.kanan)

def cetakDataLevel(subpohon, s=0):
    if subpohon is not None:
        print(subpohon.data + " Level ")
        cetakDataLevel(subpohon.kiri)
        cetakDataLevel(subpohon.kanan)
