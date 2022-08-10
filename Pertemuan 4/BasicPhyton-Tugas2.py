print('Selamat Datang!')
while True:
    print('---Menu---\n1.Daftar Kontak\n2.Tambah Kontak\n3.Keluar\n\n')
    x=int(input('Pilih Menu :'))
    daftar_contact = open('Pertemuan 4/data.txt','a')
    read_data = open('Pertemuan 4/data.txt','r')
    data = read_data.read()
    if x == 1:
        print('\nDaftar Kontak :')
        print(data)
        continue
    elif x == 2:
        while True: 
            print('Masukkan kontak baru :')
            Nama = input('Nama : ')
            number = input('No Telepon : ')
            lbl = (f'Nama : {Nama} \nNo Telpon : {number}\n\n')
            daftar_contact.write(lbl)
            print('Kontak Baru Telah Terdaftar\n')
            read_data.read()
            break
        continue
    elif x == 3:
        print('Program selesai, sampai jumpa lagi')
        read_data.close()
        break
    else :
        print('Menu tidak tersedia')
        continue    
    



        