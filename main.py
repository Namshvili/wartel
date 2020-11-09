def listToInt(awal, akhir):
    awal = awal.split(".")
    akhir = akhir.split(".")
    
    mapAwal = map(int, awal)
    mapAkhir = map(int, akhir)

    intAwal = list(mapAwal)
    intAkhir = list(mapAkhir)

    hasil = [intAwal, intAkhir]
    return hasil

def logic(jamAwal, jamAkhir, pilihHari, disc):     
    if jamAwal[0] <= 23 and jamAkhir[0] <= 23:
        if jamAwal[0] <= jamAkhir[0]:
            if jamAwal[1] <= 59 and jamAkhir[1] <= 59: 
                if jamAwal[2] <= 59 and jamAkhir[2] <= 59:
                    if pilihHari == "y" or jamAwal[0] in disc:
                        awal = (jamAwal[0] * 3600) + (jamAwal[1] * 60) + jamAwal[2]
                        akhir = (jamAkhir[0] * 3600) + (jamAkhir[1] * 60) + jamAkhir[2]
                        detik = akhir - awal
                        hasil = 7 * detik
                        print("Jumlah total pembayaran adalah : Rp. %d" %hasil)
                    else:
                        awal = (jamAwal[0] * 3600) + (jamAwal[1] * 60) + jamAwal[2]
                        akhir = (jamAkhir[0] * 3600) + (jamAkhir[1] * 60) + jamAkhir[2]
                        detik = akhir - awal
                        hasil = 10 * detik
                        print("Jumlah total pembayaran adalah : Rp. %d" %hasil)
                else:
                    hasil = print("Input Tidak Valid!!, Maks Input Detik : 59!!")
            else:
                hasil = print("Input Tidak Valid!!, Maks Input Menit : 59!!") 
        else:
            hasil = print("Input Tidak Valid!!, Jam Akhir >= Jam Awal!!") 
    else:
        hasil = print("Input Tidak Valid!!, Maks Input Jam : 23!!")

    return hasil

confirm = "y"
while confirm:
    disc  = [22, 23, 0, 1, 2, 3, 4, 5, 6]
    print("WARTEL BABEH UBET")
    awal  = input("Masukkan Jam Awal Telepon (cth: 13.15.10) : ")
    akhir = input("Masukkan Jam Akhir Telepon (cth: 13.25.10) : ")
    pilihHari = input("Apakah hari libur? (y/t) : ")

    if "." in awal and "." in akhir and len(awal) == 8 and len(akhir) == 8:
        jamInt      = listToInt(awal, akhir) 
        if pilihHari == "y" or jamInt[0][0] in disc:
            logic(jamInt[0], jamInt[1], pilihHari, disc)
        elif pilihHari == "t":
            logic(jamInt[0], jamInt[1], pilihHari,disc)
        else:
            print("Input Tidak Valid")
    else:
        print("Format Jam Salah!!") 
    
    confirm = input("Mau coba lagi ndak? (y/t) : ")
    if confirm == "t":
        break
    elif confirm == "y":
        continue
    else:
        print("Tidak Masuk Akal")

print("Terimakasih")