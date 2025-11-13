def main():
    print("==========CHƯƠNG TRÌNH NHẬP VÀ XỬ LÝ LIST THEO THỨ TỰ TĂNG==========")
    n = int(input("Nhập số phần tử của list: "))
    lst = []
    for i in range(n):
        while True:
            num = int(input(f"Nhập phần tử thứ {i + 1}: "))
            if i == 0 or num > lst[-1]:
                lst.append(num)
                break
            else:
                print("Vui lòng nhập số lớn hơn phần tử trước đó.")
    print("List sau khi nhập:", lst)
if __name__ == "__main__":
    main()