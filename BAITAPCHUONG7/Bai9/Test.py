'''Xử lý Text File - Viết phần mềm Quản Lý sản phẩm'''

'''Viết phần mềm Quản Lý sản phẩm 
Mỗi danh mục có: Mã , tên; Một danh mục có nhiều sản phẩm  
Mỗi sản phẩm có: Mã, tên, đơn giá; Mỗi một sản phẩm thuộc về một danh mục. 
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File '''

from XuLyFile import * 
from SanPham import *
from DanhMuc import *
import os
import json
def Menu():
    print("-----QUẢN LÝ SẢN PHẨM-----")
    print("1. Thêm danh mục")
    print("2. Thêm sản phẩm")
    print("3. Hiển thị danh mục và sản phẩm")
    print("4. Tìm kiếm sản phẩm theo tên")
    print("5. Sắp xếp sản phẩm theo đơn giá")
    print("6. Lưu dữ liệu ra file")
    print("7. Đọc dữ liệu từ file")
    print("8. Xóa sản phẩm theo mã")
    print("9. Sửa sản phẩm theo mã")
    print("0. Thoát")
    choice = input("Chọn chức năng: ")
    return choice

danhMucList = []
while True:
    os.system('cls')
    choice = Menu()
    if choice == '1':
        # Thêm danh mục
        ma = input("Nhập mã danh mục: ")
        ten = input("Nhập tên danh mục: ")
        danhMuc = DanhMuc(ma, ten)
        danhMucList.append(danhMuc)
        print("Đã thêm danh mục.")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '2':
        # Thêm sản phẩm
        maDM = input("Nhập mã danh mục của sản phẩm: ")
        danhMuc = next((dm for dm in danhMucList if dm.ma == maDM), None)
        if danhMuc:
            maSP = input("Nhập mã sản phẩm: ")
            tenSP = input("Nhập tên sản phẩm: ")
            donGia = float(input("Nhập đơn giá sản phẩm: "))
            sanPham = SanPham(maSP, tenSP, donGia)
            danhMuc.themSanPham(sanPham)
            print("Đã thêm sản phẩm.")
        else:
            print("Danh mục không tồn tại.")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '3':
        # Hiển thị danh mục và sản phẩm
        for dm in danhMucList:
            print(f"Danh mục: {dm.ma} - {dm.ten}")
            for sp in dm.sanPhamList:
                print(f"  Sản phẩm: {sp.ma} - {sp.ten} - {sp.donGia}")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '4':
        # Tìm kiếm sản phẩm theo tên
        tenTimKiem = input("Nhập tên sản phẩm cần tìm: ")
        for dm in danhMucList:
            for sp in dm.sanPhamList:
                if tenTimKiem.lower() in sp.ten.lower():
                    print(f"Tìm thấy: {sp.ma} - {sp.ten} - {sp.donGia} trong danh mục {dm.ten}")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '5':
        # Sắp xếp sản phẩm theo đơn giá
        for dm in danhMucList:
            dm.sanPhamList.sort(key=lambda sp: sp.donGia)
        print("Đã sắp xếp sản phẩm theo đơn giá.")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '6':
        # Lưu dữ liệu ra file
        dataToSave = [dm.toDict() for dm in danhMucList]
        jsonString = json.dumps(dataToSave, ensure_ascii=False, indent=4)
        GhiFile("danhmuc_sanpham.txt", [jsonString])
        print("Đã lưu dữ liệu ra file.")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '7':
        # Đọc dữ liệu từ file và hiển thị
        if not os.path.exists("danhmuc_sanpham.txt"):
            print("File không tồn tại hoặc chưa có dữ liệu.")
            input("Nhấn Enter để tiếp tục...")
            continue # Quay lại vòng lặp while

        try:
            # Mở file và đọc TOÀN BỘ nội dung
            with open("danhmuc_sanpham.txt", 'r', encoding='utf-8') as f:
                full_json_string = f.read()

            # Kiểm tra xem file có rỗng không
            if not full_json_string:
                print("File rỗng.")
                input("Nhấn Enter để tiếp tục...")
                continue # Quay lại vòng lặp while

            # Giải mã toàn bộ chuỗi JSON
            dataLoaded = json.loads(full_json_string)
            
            danhMucList = [DanhMuc.fromDict(dmData) for dmData in dataLoaded]
            
            print("Dữ liệu danh mục và sản phẩm đã đọc từ file:")
            for dm in danhMucList:
                print(f"Danh mục: {dm.ma} - {dm.ten}")
                for sp in dm.sanPhamList:
                    print(f"  Sản phẩm: {sp.ma} - {sp.ten} - {sp.donGia}")

        except json.JSONDecodeError:
            print("Lỗi: Không thể giải mã dữ liệu từ file. File có thể bị hỏng.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
            
        input("Nhấn Enter để tiếp tục...")
    elif choice == '8':
        # Xóa sản phẩm theo mã
        maSPXoa = input("Nhập mã sản phẩm cần xóa: ")
        found = False
        for dm in danhMucList:
            for sp in dm.sanPhamList:
                if sp.ma == maSPXoa:
                    dm.xoaSanPham(maSPXoa)
                    found = True
                    print("Đã xóa sản phẩm.")
                    break
            if found:
                break
        if not found:
            print("Không tìm thấy sản phẩm với mã đã cho.")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '9':
        # Sửa sản phẩm theo mã
        maSPSua = input("Nhập mã sản phẩm cần sửa: ")
        found = False
        for dm in danhMucList:
            for sp in dm.sanPhamList:
                if sp.ma == maSPSua:
                    tenMoi = input("Nhập tên sản phẩm mới: ")
                    donGiaMoi = float(input("Nhập đơn giá sản phẩm mới: "))
                    sp.ten = tenMoi
                    sp.donGia = donGiaMoi
                    found = True
                    print("Đã sửa sản phẩm.")
                    break
            if found:
                break
        if not found:
            print("Không tìm thấy sản phẩm với mã đã cho.")
        input("Nhấn Enter để tiếp tục...")
    elif choice == '0':
        # Thoát
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        input("Nhấn Enter để tiếp tục...")
        