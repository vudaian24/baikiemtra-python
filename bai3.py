print("Nhập một số: ")
a = input("")
tong = 0
tich = 1
if(int(a) < 0):
    print("Nhập lại a!!!")
else:
    for i in range(0, int(a), 1):
        tong = tong + 1
        tich = tich * tong
    print("Giai thừa của", a, "là: ",tich)