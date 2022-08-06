
value_1 = float(input("Masukkan Nilai Ujian Teori : "))
value_2 = float(input("Masukkan Nilai Ujian Praktek : "))

if value_1 > 70 and value_2 > 70:
    print("Selamat, anda lulus!")
elif value_1 > 70 and value_2 < 70:
    print("Anda Haru mengulang ujian praktek.")
elif value_1 < 70 and value_2 > 70:
    print("Anda harus mengulang ujian teori")
elif value_1 < 70 and value_2 < 70:
    print("Anda harus mengulang ujian teori dan praktek")