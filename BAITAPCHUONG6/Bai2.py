from random import randrange

def is_symmetric(lst):
    return lst == lst[::-1]

def main():
    print("==========CHƯƠNG TRÌNH XỬ LÝ LIST NHẬP NGẪU NHIÊN==========")

    n = int(input("Nhập số phần tử của list: "))
    lst = [randrange(-100, 100) for _ in range(n)]
    print("List ngẫu nhiên:", lst)

    k = int(input("Nhập số k để xóa khỏi list: "))
    lst = [x for x in lst if x != k]
    print(f"List sau khi xóa tất cả các phần tử có giá trị {k}:", lst)

    if is_symmetric(lst):
        print("List là đối xứng.")
    else:
        print("List không là đối xứng.")

if __name__ == "__main__":
    main()