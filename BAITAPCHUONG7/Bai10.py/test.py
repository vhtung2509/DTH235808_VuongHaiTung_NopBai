from XuLyFile import *
from SinhVien import *
from LopHoc import *
import os
import json

def Menu():
    print("-----QUẢN LÝ SINH VIÊN-----")
    print("1. Thêm lớp học")
    print("2. Thêm sinh viên")
    print("3. Hiển thị lớp học và sinh viên")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo năm sinh")
    print("6. Lưu dữ liệu ra file")
    print("7. Đọc dữ liệu từ file")
    print("8. Xóa sinh viên theo mã")
    print("9. Sửa sinh viên theo mã")
    print("0. Thoát")
    choice = input("Chọn chức năng: ")
    return choice

lopHocList = []
while True:
    os.system('cls')
    choice = Menu()
    
    if choice == '1':
        # Thêm lớp học
        ma = input("Nhập mã lớp học: ")
        ten = input("Nhập tên lớp học: ")
        lopHoc = LopHoc(ma, ten)
        lopHocList.append(lopHoc)
        print("Đã thêm lớp học.")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '2':
        # Thêm sinh viên
        maLH = input("Nhập mã lớp học của sinh viên: ")
        lopHoc = next((lh for lh in lopHocList if lh.maLop == maLH), None)
        if lopHoc:
            maSV = input("Nhập mã sinh viên: ")
            tenSV = input("Nhập tên sinh viên: ")
            namSinh = int(input("Nhập năm sinh sinh viên: "))
            sinhVien = SinhVien(maSV, tenSV, namSinh)
            lopHoc.themSinhVien(sinhVien)
            print("Đã thêm sinh viên.")
        else:
            print("Lớp học không tồn tại.")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '3':
        # Hiển thị lớp học và sinh viên
        for lh in lopHocList:
            print(f"Lớp học: {lh.ma} - {lh.ten}")
            for sv in lh.sinhVienList:
                print(f"  Sinh viên: {sv.ma} - {sv.ten} - {sv.namSinh}")
        input("Nhấn Enter để tiếp tục...")
        
    elif choice == '4':
        # Tìm kiếm sinh viên theo tên
        tenTimKiem = input("Nhập tên sinh viên cần tìm: ")
        for lh in lopHocList:
            for sv in lh.sinhVienList:
                if tenTimKiem.lower() in sv.ten.lower():
                    print(f"Tìm thấy sinh viên: {sv.ma} - {sv.ten} - {sv.namSinh} trong lớp {lh.ma}")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '5':
        # Sắp xếp sinh viên theo năm sinh
        for lh in lopHocList:
            lh.sinhVienList.sort(key=lambda sv: sv.namSinh)
        print("Đã sắp xếp sinh viên theo năm sinh.")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '6':
        # Lưu dữ liệu ra file
        try:
            data = [lh.to_dict() for lh in lopHocList]
            LuuFileJSON('dulieu_sinhvien.json', data)
            print("Đã lưu dữ liệu ra file dulieu_sinhvien.json")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '7':
        # Đọc dữ liệu từ file và hiển thị
        try:
            # Giả sử DocFileJSON đọc và trả về nội dung JSON đã parse
            data = DocFileJSON('dulieu_sinhvien.json')
            
            if not data:
                print("File 'dulieu_sinhvien.json' rỗng hoặc không tìm thấy.")
            else:
                lopHocList = [LopHoc.from_dict(lh_data) for lh_data in data]
                
                print("--- DỮ LIỆU ĐỌC TỪ FILE ---")
                
                for lh in lopHocList:
                    
                    print(f"Lớp: {lh.maLop} - {lh.tenLop}") 
                    
                    for sv in lh.sinhVienList:
                        print(f"  Sinh viên: {sv.ma} - {sv.ten} - {sv.namSinh}")
                
                print("------------------------------")
                print("Đã đọc và hiển thị dữ liệu thành công.")

        except FileNotFoundError:
             print("Lỗi: Không tìm thấy file 'dulieu_sinhvien.json'.")
        except Exception as e:
            # In lỗi chi tiết hơn (ví dụ: lỗi 'from_dict' không tồn tại)
            print(f"Đã xảy ra lỗi khi xử lý dữ liệu: {e}") 
            
        # Thêm input để tạm dừng màn hình (như các chức năng khác)
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '8':
        # Xóa sinh viên theo mã
        maSV = input("Nhập mã sinh viên cần xóa: ")
        found = False
        for lh in lopHocList:
            for sv in lh.sinhVienList:
                if sv.ma == maSV:
                    lh.sinhVienList.remove(sv)
                    found = True
                    print("Đã xóa sinh viên.")
                    break
            if found:
                break
        if not found:
            print("Không tìm thấy sinh viên với mã đã cho.")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '9':
        # Sửa sinh viên theo mã
        maSV = input("Nhập mã sinh viên cần sửa: ")
        found = False
        for lh in lopHocList:
            for sv in lh.sinhVienList:
                if sv.ma == maSV:
                    tenMoi = input("Nhập tên mới cho sinh viên: ")
                    namSinhMoi = int(input("Nhập năm sinh mới cho sinh viên: "))
                    sv.ten = tenMoi
                    sv.namSinh = namSinhMoi
                    found = True
                    print("Đã sửa thông tin sinh viên.")
                    break
            if found:
                break
        if not found:
            print("Không tìm thấy sinh viên với mã đã cho.")
        input("Nhấn Enter để tiếp tục...")
    
    elif choice == '0':
        # Thoát
        break