def dem_ky_tu(s):
    hoa = thuong = so = dacbiet = khoangtrang = nguyenam = phuam = 0
    nguyen_am = "aeiouAEIOU"
    for ch in s:
        if ch.isupper():
            hoa += 1
        elif ch.islower():
            thuong += 1
        if ch.isdigit():
            so += 1
        elif not ch.isalnum() and ch != " ":
            dacbiet += 1
        elif ch == " ":
            khoangtrang += 1
        if ch.lower() in nguyen_am:
            nguyenam += 1
        elif ch.isalpha() and ch.lower() not in nguyen_am:
            phuam += 1
    return hoa, thuong, so, dacbiet, khoangtrang, nguyenam, phuam

def main():
    s = input("Nhập chuỗi: ")
    hoa, thuong, so, dacbiet, khoangtrang, nguyenam, phuam = dem_ky_tu(s)
    print("-" * 30)
    print("Số chữ IN HOA:", hoa)
    print("Số chữ in thường:", thuong)
    print("Số chữ là chữ số:", so)
    print("Số chữ là ký tự đặc biệt:", dacbiet)
    print("Số chữ là khoảng trắng:", khoangtrang)
    print("Số chữ là nguyên âm:", nguyenam)
    print("Số chữ là phụ âm:", phuam)
main()

