from random import randrange

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    print("==========CHƯƠNG TRÌNH XỬ LÝ MẢNG==========")
    n = int(input("Nhập số phần tử của mảng: "))
    M = [randrange(1, 100) for _ in range(n)]
    print("Mảng ngẫu nhiên:", M)

    le = [x for x in M if x % 2 != 0]
    chan = [x for x in M if x % 2 == 0]
    nguyen_to = [x for x in M if is_prime(x)]
    khong_nguyen_to = [x for x in M if not is_prime(x)]

    print(f"Số lẻ: {le}, Tổng số lẻ: {len(le)}")
    print(f"Số chẵn: {chan}, Tổng số chẵn: {len(chan)}")
    print(f"Số nguyên tố: {nguyen_to}")
    print(f"Số không phải nguyên tố: {khong_nguyen_to}")

if __name__ == "__main__":
    main()