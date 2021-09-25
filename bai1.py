list1 = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
print("Danh sách 1: ")
print(list1)
print("")
print("Danh sách 2: ")
for i in range(0, 15):
    if(list1[i] < 30):
        list2 = list1[i]
        print(list2, end="  ")
print("")
print("Nhập a: ")
a = input("")
print("Những số nhỏ hơn", a ,"là: ")
for i in range(0, 15):
    if(list1[i] < int(a)):
        list3 = list1[i]
        print(list3, end="  ")
