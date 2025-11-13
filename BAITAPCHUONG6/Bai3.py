from random import randrange

def nhap_ma_tran(m, n):
    ma_tran = []
    for i in range(m):
        dong = []
        for j in range(n):
            dong.append(randrange(-100, 100))
        ma_tran.append(dong)
    return ma_tran

def xuat_ma_tran(ma_tran):
    for dong in ma_tran:
        print(dong)

def xuat_dong(ma_tran, dong_so):
    if 0 <= dong_so < len(ma_tran):
        print(f"Dòng {dong_so}: {ma_tran[dong_so]}")
    else:
        print("Số dòng không hợp lệ.")

def xuat_cot(ma_tran, cot_so):
    if 0 <= cot_so < len(ma_tran[0]):
        cot = [ma_tran[i][cot_so] for i in range(len(ma_tran))]
        print(f"Cột {cot_so}: {cot}")
    else:
        print("Số cột không hợp lệ.")

def tim_so_max(ma_tran):
    so_max = ma_tran[0][0]
    for dong in ma_tran:
        for gia_tri in dong:
            if gia_tri > so_max:
                so_max = gia_tri
    return so_max

def main():
    print("==========CHƯƠNG TRÌNH XỬ LÝ MA TRẬN==========")

    m = int(input("Nhập số dòng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))
    ma_tran = nhap_ma_tran(m, n)
    
    print("Ma trận ngẫu nhiên:")
    xuat_ma_tran(ma_tran)

    dong_so = int(input("Nhập số dòng cần xuất (bắt đầu từ 0): "))
    xuat_dong(ma_tran, dong_so)

    cot_so = int(input("Nhập số cột cần xuất (bắt đầu từ 0): "))
    xuat_cot(ma_tran, cot_so)

    so_max = tim_so_max(ma_tran)
    print(f"Số MAX trong ma trận là: {so_max}")

if __name__ == "__main__":
    main()