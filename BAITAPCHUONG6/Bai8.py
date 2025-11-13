def main():
    print("==========CHƯƠNG TRÌNH NHẬP VÀ XỬ LÝ LIST THEO THỨ TỰ GIẢM==========")
    n = int(input("Nhập số phần tử của list: "))
    lst = []
    for i in range(n):
        num = float(input(f"Nhập phần tử thứ {i + 1}: "))
        lst.append(num)
    lst.sort(reverse=True)
    print("List sau khi sắp xếp giảm dần:", lst)
if __name__ == "__main__":
    main()