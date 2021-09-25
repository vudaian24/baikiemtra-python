print("Nhập số nguyên dương: ")
n = int(input(" "))
def A(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
print("Tổng các chữ số của", n, "là", A(n));