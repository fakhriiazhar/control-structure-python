# if elif expression
kelas = input("kelas berapa anda sekarang? ")
kelas = int(kelas)
if kelas < 6 :
    print("anda masih di SD")
elif kelas >= 7 and kelas <= 9 :
    print("anda di SMP")
elif kelas >=10 and kelas <= 12 :
    print("anda di SMA")
elif kelas > 12 :
    print("anda sudah lulus")
