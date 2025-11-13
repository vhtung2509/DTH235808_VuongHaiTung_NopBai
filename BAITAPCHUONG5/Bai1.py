# Kiểm tra chuỗi đối xứng
def Kiem_tra_chuoi_doi_xung(s):
    flag=True 
    for i in range(len(s)): 
     if s[i]!=s[len(s)-i-1]: 
          flag=False 
          break 
    return flag 

def main():
    print("Nhập 1 chuỗi:") 
    s=input() 
    if(Kiem_tra_chuoi_doi_xung(s)): 
        print("Chuỗi bạn nhập là chuỗi đối xứng") 
    else: 
        print("Chuỗi bạn nhập là chuỗi không đối xứng")

while True:
    main()
    print("Bạn có muốn tiếp tục không?(c/k):") 
    s=input() 
    if s=="k": 
        break 
    print("Cảm ơn bạn!")