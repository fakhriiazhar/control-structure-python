#else expression
badan = float(input("berapa tinggi badan anda? "))
if badan < 154:
    print("anda terlalu pendek")
elif badan >= 154 and badan < 165 :
    print("cukup ideal")
elif badan >= 166 and badan < 170 :
    print("ideal")
elif badan >= 171 and badan < 176 :
    print("cukup tinggi")
else :
    print("abnormal/berlebih")
