#Chương trình tối ưu chuỗi
def Toi_uu_chuoi(s):
    s1=s 
    s1=s1.strip() 
    arr=s1.split(' ') 
    s1="" 
    for x in arr: 
        word=x 
        if len(word.strip())!=0: 
            s1=s1+word+" " 
    return s1.strip()

def main():
    print("Nhap 1 chuỗi: ")
    string=input()

    print("Chuỗi đã tối ưu",Toi_uu_chuoi(string))

main()