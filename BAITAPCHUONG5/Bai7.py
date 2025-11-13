def ToiUuChuoi(s):
    s = s.strip()                     
    words = s.split()                 
    words = [w.capitalize() for w in words] 
    return " ".join(words)     

# Chương trình chính
def main():
    s = input("Nhập chuỗi: ")
    print("Chuỗi tối ưu:", ToiUuChuoi(s))


main()
