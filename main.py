import modul as md
while True:
    md.tampilan()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        md.insert()
        lanjut = input('APAKAH ANDA INGIN KEMBALI KE MENU (Y/N) : ').upper()
        if lanjut=='y'.upper():
            continue
        else:
            md.end()
            exit()

    elif pilihan == 2:
        md.edit()
        lanjut = input('APAKAH ANDA INGIN KEMBALI KE MENU (Y/N) : ').upper()
        if lanjut=='y'.upper():
            continue
        else:
            md.end()
            exit()

    elif pilihan == 3:
        md.delete()
        lanjut = input('APAKAH ANDA INGIN KEMBALI KE MENU (Y/N) : ').upper()
        if lanjut=='y'.upper():
            continue
        else:
            md.end()
            exit()

    elif pilihan == 4:
        md.search()
        lanjut = input('APAKAH ANDA INGIN KEMBALI KE MENU (Y/N) : ').upper()
        if lanjut=='y'.upper():
            continue
        else:
            md.end()
            exit()

    elif pilihan == 5:
        md.display()
        lanjut = input('APAKAH ANDA INGIN KEMBALI KE MENU (Y/N) : ').upper()
        if lanjut=='y'.upper():
            continue
        else:
            md.end()
            exit()

    elif pilihan == 6:
        md.total()
        lanjut = input('APAKAH ANDA INGIN KEMBALI KE MENU (Y/N) : ').upper()
        if lanjut=='y'.upper():
            continue
        else:
            md.end()
            exit()

    else:
        md.end()
        exit()