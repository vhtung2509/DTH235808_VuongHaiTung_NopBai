from xml.dom.minidom import parse
import xml.dom.minidom
import os   

def Menu():
    print("-----QUẢN LÝ THIẾT BỊ-----")
    print("1. Hiển thị danh sách Nhóm thiết bị")
    print("2. Hiển thị toàn bộ Thiết bị")
    print("3. Lọc Danh sách Thiết bị theo Nhóm thiết bị")
    print("4. Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất")
    print("0. Thoát")
    choice = input("Chọn chức năng: ")
    return choice

while True:
    os.system('cls')
    choice = Menu()
    
    if choice == '1':
        # Hiển thị danh sách Nhóm thiết bị
        try:
            DOMTree = xml.dom.minidom.parse("nhomthietbi.xml")
            nhoms = DOMTree.documentElement
            nhomList = nhoms.getElementsByTagName("nhom")
            print("Danh sách Nhóm thiết bị:")
            for nhom in nhomList:
                ma = nhom.getElementsByTagName("ma")[0].childNodes[0].data
                ten = nhom.getElementsByTagName("ten")[0].childNodes[0].data
                print(f"Mã: {ma}, Tên: {ten}")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file: {e}")
        
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '2':
        # Hiển thị toàn bộ Thiết bị
        try:
            DOMTree = xml.dom.minidom.parse("ThietBi.xml")
            thietbis = DOMTree.documentElement
            thietbiList = thietbis.getElementsByTagName("thietbi")
            print("Danh sách Thiết bị:")
            for thietbi in thietbiList:
                manhom = thietbi.getAttribute("manhom")
                ma = thietbi.getElementsByTagName("ma")[0].childNodes[0].data
                ten = thietbi.getElementsByTagName("ten")[0].childNodes[0].data
                print(f"Mã Nhóm: {manhom}, Mã Thiết bị: {ma}, Tên Thiết bị: {ten}")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file: {e}")
            
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '3':
        # Lọc Danh sách Thiết bị theo Nhóm thiết bị
        manhom_filter = input("Nhập Mã Nhóm thiết bị để lọc: ")
        try:
            DOMTree = xml.dom.minidom.parse("ThietBi.xml")
            thietbis = DOMTree.documentElement
            thietbiList = thietbis.getElementsByTagName("thietbi")
            print(f"Danh sách Thiết bị trong Nhóm {manhom_filter}:")
            
            for thietbi in thietbiList:
                manhom = thietbi.getAttribute("manhom")
                if manhom == manhom_filter:
                    ma = thietbi.getElementsByTagName("ma")[0].childNodes[0].data
                    ten = thietbi.getElementsByTagName("ten")[0].childNodes[0].data
                    print(f"Mã Thiết bị: {ma}, Tên Thiết bị: {ten}")
                    
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file: {e}")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '4':
        # Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất
        try:
            DOMTree = xml.dom.minidom.parse("ThietBi.xml")
            thietbis = DOMTree.documentElement
            thietbiList = thietbis.getElementsByTagName("thietbi")
            group_count = {}
            for thietbi in thietbiList:
                manhom = thietbi.getAttribute("manhom")
                if manhom in group_count:
                    group_count[manhom] += 1
                else:
                    group_count[manhom] = 1
            max_group = max(group_count, key=group_count.get)
            print(f"Nhóm thiết bị có số lượng thiết bị nhiều nhất là: {max_group} với {group_count[max_group]} thiết bị.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file: {e}")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '0':
        # Thoát
        break
            

