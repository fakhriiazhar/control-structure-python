#nested control structure
x = int(input("masukan nilai x = "))
y = int(input("masukan nilai y = "))

if x == y :
    print("x dan y bernilai sama")
else:
    print("x dan y bernilai berbeda")
    if x >= y :
        print("x lebih besar atau sama dengan y")
    else:
        print("x kurang dari atau sama dengan")
