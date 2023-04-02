print ("Nama : Safal")
print ("NIM : E1E120048")
print ("Program Fungsi Keanggotaan")
print ("===========================")

import math

print ("Jenis-Jenis Fungsi Keanggotaan")
jfks=[("1", 'Linear'), ("2", 'Segitiga'), ("3", 'Trapesium'), ("4", 'Sigmoid'), ("5", 'Gauss'), ("6", 'Beta')]
nomor = 0
for isi in jfks:
    nomor += 1
    print(isi[0], ".", isi[1])
kondisi="masuk"
while kondisi=="masuk":
    kondisi="keluar"
    jfkinput=input("Masukan Jenis (cth: '1' atau 'Linear'): ").lower()
    if (jfkinput == jfks[0][0] or jfkinput == jfks[0][1].lower()):
        print("Fungsi Linear ")
        kdslinear="masuk"
        while kdslinear=="masuk":
            kdslinear="keluar"
            jfklinear=input("Masukan Jenis Linear ('Naik' atau 'turun'): ").lower()
            if(jfklinear=="turun"):
                a=float(input("Masukan titik a (nilai derajat keanggotaan = 1) : "))
                b=float(input("Masukan titik b (nilai derajat keanggotaan = 0) : "))
                x=float(input("Masukan titik x yang akan dihitung derajat keanggotaannya : "))
                if(x<=a): m=1
                elif(x>a and x<b): m=(b-x)/(b-a)
                else: m=0
                print ("Derajat Keanggotaan ", x, " adalah ", round(m,3))
            elif(jfklinear=="naik"):
                a=float(input("Masukan nilai a (nilai derajat keanggotaan 0) : "))
                b=float(input("Masukan nilai b (nilai derajat keanggotaan 1) : "))
                x=float(input("Masukan nilai x yang akan dihitung derajat keanggotaanya : "))
                if(x<=a): m=0
                elif(x>a and x<b): m=(x-a)/(b-a)
                else: m=1
                print("Derajat Keanggotaan ", x, " adalah ", round(m,3))
            else:
                kdslinear="masuk"
                print("jenis linear yang anda masukan tidak ada perhatikan kembali penulisan jenis fungsi anda")
    elif (jfkinput == jfks[1][0] or jfkinput == jfks[1][1].lower()):
        print("Fungsi Segitiga")
        a=float(input("masukan nilai a (nilai derajat keanggotaan 0) : "))
        b=float(input("masukan nilai b (nilai derajat keanggotaan 1) : "))
        c=float(input("masukan nilai c (nilai derajat keanggotaan kembali 0) : "))
        x=float(input("Masukan nilai x yang akan dihitung derajat keanggotannya : "))
        if(x<=a and x>=c): m=0
        elif(x>a and x<b): m=(x-a)/(b-a)
        elif(x==b): m=1
        else: m=(c-x)/(c-b)
        print("Derajat Keanggotaan ", x, " adalah ", round(m,3))
    elif (jfkinput == jfks[2][0] or jfkinput == jfks[2][1].lower()):
        print("Fungsi Trapesium")
        a=float(input("masukan nilai a (nilai derajat keanggotaan 0) : "))
        b=float(input("masukan nilai b (nilai awal derajat keanggotaan 1) : "))
        c=float(input("masukan nilai c (nilai akhir derajat keanggotaan 1) : "))
        d=float(input("masukan nilai d (nilai derajat keanggotaan kembali 0) : "))
        x=float(input("Masukan nilai x yang akan dihitung derajat keanggotannya : "))
        if(x<=a and x>=d): m=0
        elif(x>a and x<b): m=(x-a)/(b-a)
        elif(x>=b and x<=c): m=1
        else: m=(c-x)/(c-b)
        print("Derajat Keanggotaan ", x, " adalah ", round(m,3))
    elif (jfkinput == jfks[3][0] or jfkinput == jfks[3][1].lower()):
        print("Fungsi Sigmoid")
        kdssigmoid="masuk"
        while kdssigmoid=="masuk":
            kdssigmoid="keluar"
            jfksigmoid=input("Masukan jenis kurva sigmoid (Penyusutan atau pertumbuhan) : ").lower()
            if(jfksigmoid=="pertumbuhan"):
                print("Fungsi Sigmoid S pertumbuhan")
                a=float(input("Masukan nilai Alpha (nilai derajat keanggotaan 0) : "))
                y=float(input("Masukan nilai Gamma (nilai derajat keanggotaan 1) : "))
                b=a+((y-a)/2)
                x=float(input("Masukan nilai x yang akan dihitung derajat keanggotaannya : "))
                if (x<=a): m=0
                elif (x>a and x<=b): m=2*(((x-a)/(y-a))**2)
                elif (x>b and x<y): m=1-2*(((y-x)/(y-a))**2)
                else: m=1
                print ("Derajat Keanggotaan ", x, " adalah ", round(m,3))
            elif(jfksigmoid=="penyusutan"):
                print("Fungsi Sigmoid S penyusutan")
                a=float(input("Masukan nilai Alpha (nilai derajat keanggotaan 1) : "))
                y=float(input("Masukan nilai Gamma (nilai derajat keanggotaan 0) : "))
                b=a+((y-a)/2)
                x=float(input("Masukan nilai x yang akan dihitung derajat keanggotaannya : "))
                if (x<=a): m=1
                elif (x>a and x<=b): m=1-2*(((x-a)/(y-a))**2)
                elif (x>b and x<y): m=2*(((y-x)/(y-a))**2)
                else: m=0
                print ("Derajat Keanggotaan ", x, " adalah ", round(m,3))
            else:
                kdssigmoid="masuk"
                print("jenis kurva sigmoid yang anda masukan tidak ada, perhatikan kembali penulisan anda")
    elif (jfkinput == jfks[4][0] or jfkinput == jfks[4][1].lower()):
        print("Fungsi Gauss")
        a=float(input("masukan titik awal domain : "))
        b=float(input("masukan titik akhir domain : "))
        k=(b-a)/2
        y=a+k
        x=float(input('Masukan nilai x yang akan dihitung derajat keanggotaannya : '))
        print("titip pusat kurva : ", y, " dan lebar kurva : ", k)
        G= 2.7182**(-0.5*(((x-y)/k)**2))
        print("Derajat Keanggotaan ", x, " adalah ", round(G,3))
    elif (jfkinput == jfks[5][0] or jfkinput == jfks[5][1].lower()):
        print("Fungsi Beta")
        a=float(input("Masukan titik awal domain : "))
        ad=float(input("Masukan titik akhir domain : "))
        y=((ad-a)/2)+a
        b=(y-a)/2
        x=float(input("Masukan nilai X yang akan dihitung derajat keanggotaannya : "))
        B=1/(1+(((x-y)/b)**2))
        print("Derajat Keanggotaan ", x, " adalah ", round(B,3))
    else:
        kondisi="masuk"
        print("Jenis yang anda masukan tidak ada")
        print("perhatikan kembali inputan anda")