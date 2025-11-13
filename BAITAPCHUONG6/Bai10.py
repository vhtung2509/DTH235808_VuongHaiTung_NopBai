'''Xử lý Ma Trận '''
'''Yêu cầu: 
Nhập 2 matrix A, B. 
Cộng 2 matrix 
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B '''

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

def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        dong = []
        for j in range(n):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C

def hoan_vi_ma_tran(ma_tran):
    m = len(ma_tran)
    n = len(ma_tran[0])
    hoan_vi = []
    for j in range(n):
        dong = []
        for i in range(m):
            dong.append(ma_tran[i][j])
        hoan_vi.append(dong)
    return hoan_vi

def main():
    print("==========CHƯƠNG TRÌNH XỬ LÝ MA TRẬN==========")

    m = int(input("Nhập số dòng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    print("Nhập ma trận A:")
    A = nhap_ma_tran(m, n)
    xuat_ma_tran(A)

    print("Nhập ma trận B:")
    B = nhap_ma_tran(m, n)
    xuat_ma_tran(B)

    C = cong_ma_tran(A, B)
    print("Ma trận C (A + B):")
    xuat_ma_tran(C)

    A_hoan_vi = hoan_vi_ma_tran(A)
    print("Ma trận hoán vị của A:")
    xuat_ma_tran(A_hoan_vi)

    B_hoan_vi = hoan_vi_ma_tran(B)
    print("Ma trận hoán vị của B:")
    xuat_ma_tran(B_hoan_vi)

if __name__ == "__main__":
    main()

