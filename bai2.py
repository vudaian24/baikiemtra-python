list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 88]
list2 = [1, 3, 5, 4, 7, 88, 66, 59, 40, 54]
print("Danh sách 1: ", list1)
print("Danh sách 2: ", list2)

list3 = set(list1) & set(list2)
print("Danh sách các phần tử giống nhau trong hai danh sách: ")
for i in list3:
    print(i, end="  ")

list4 = set(list1) - set(list3)
print("")
print("Danh sách các phần tử còn lại trong danh sách 1: ")
for i in list4:
    print(i, end="  ")

list5 = set(list2) - set(list3)
print("")
print("Danh sách các phần tử còn lại trong danh sách 2: ")
for i in list5:
    print(i, end="  ")