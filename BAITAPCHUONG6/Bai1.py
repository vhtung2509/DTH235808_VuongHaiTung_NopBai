from random import randrange

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("==========CHƯƠNG TRÌNH XỬ LÝ LIST==========")

    n = int(input("Nhập số phần tử của list: "))
    lst = [0] * n
    for i in range(n):
        lst[i] = randrange(-100, 100)
    print("List ngẫu nhiên:", lst)

    print("Mời bạn thêm phần tử vào list: ")
    x = int(input("Nhập số x cần thêm: "))
    lst.append(x)
    print("List sau khi thêm:", lst)

    k = int(input("Nhập số k để kiểm tra số lần xuất hiện trong list: "))
    count_k = lst.count(k)
    print(f"Số {k} xuất hiện {count_k} lần trong list.")

    sum_primes = sum(x for x in lst if is_prime(x))
    print(f"Tổng các số nguyên tố trong list là: {sum_primes}")

    lst.sort()
    print("List sau khi sắp xếp:", lst)

    lst.clear()
    print("List sau khi xóa:", lst)

if __name__ == "__main__":
    main()