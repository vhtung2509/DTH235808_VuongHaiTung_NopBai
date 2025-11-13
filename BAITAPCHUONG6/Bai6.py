from random import sample

print("==========CHƯƠNG TRÌNH NHẬP VÀ XỬ LÝ LIST KHÔNG TRÙNG NHAU==========")
n = int(input("Nhập số phần tử của list: "))
lst = sample(range(-100, 100), n)  # Tạo list ngẫu nhiên không trùng nhau
print("List ngẫu nhiên không trùng nhau:", lst)

