import os

def LayTenFile(duongdan):
    return os.path.basename(duongdan)   # Lấy tên file + đuôi mở rộng

def LayTenBaiHat(duongdan):
    ten_file = os.path.basename(duongdan)
    ten_bai_hat, _ = os.path.splitext(ten_file)  # Tách bỏ phần mở rộng
    return ten_bai_hat

# Ví dụ sử dụng
duongdan = r"d:\music\muabui.mp3"
print("Tên file:", LayTenFile(duongdan))
print("Tên bài hát:", LayTenBaiHat(duongdan))
