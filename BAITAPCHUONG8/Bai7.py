import tkinter as tk

def convert_gregorian_to_lunar():
    """
    Lấy năm từ ô input, tính toán Can Chi, và cập nhật
    nhãn kết quả.
    """
    
    # Danh sách 10 Thiên Can
    # Index 0 tương ứng với năm có số cuối là 0 (Canh)
    # Index 1 tương ứng với năm có số cuối là 1 (Tân)
    # Index 2 tương ứng với năm có số cuối là 2 (Nhâm) ...
    list_can = [
        "Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", 
        "Bính", "Đinh", "Mậu", "Kỷ"
    ]
    
    # Danh sách 12 Địa Chi
    # Index 0 tương ứng với Tý (ví dụ: 1984 % 12 = 4, offset là -4)
    # (year + 8) % 12 sẽ cho đúng index
    list_chi = [
        "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", 
        "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"
    ]

    try:
        # 1. Lấy năm từ ô nhập liệu
        year_str = entry_duong.get()
        if not year_str:
            label_ketqua.config(text="Chưa nhập năm!")
            return
            
        year = int(year_str)

        # 2. Tính toán Can (dựa trên chữ số cuối)
        can_index = year % 10
        can_name = list_can[can_index]

        # 3. Tính toán Chi (dựa trên phép chia 12)
        # Dùng mốc 1984 (Giáp Tý) -> (1984 + 8) % 12 = 1992 % 12 = 0
        # 1982 (Nhâm Tuất) -> (1982 + 8) % 12 = 1990 % 12 = 10 (index của Tuất)
        chi_index = (year + 8) % 12 
        chi_name = list_chi[chi_index]

        # 4. Hiển thị kết quả
        result = f"{can_name} {chi_name}"
        label_ketqua.config(text=result)

    except ValueError:
        # Xử lý nếu người dùng nhập không phải là số
        label_ketqua.config(text="Vui lòng nhập số!")
    except Exception as e:
        label_ketqua.config(text=f"Lỗi: {e}")

# --- Cài đặt cửa sổ chính (root) ---
root = tk.Tk()
root.title("Chuyển năm Dương Lịch - Âm Lịch")
root.geometry("400x200") # (Rộng x Cao)


BACKGROUND_COLOR = "#FFFF00" 
root.config(bg=BACKGROUND_COLOR)

# --- Tạo các widget ---


label_duong = tk.Label(
    root, 
    text="Nhập năm dương:", 
    bg=BACKGROUND_COLOR, # Đặt nền vàng
    font=('Arial', 12)
)


entry_duong = tk.Entry(
    root, 
    font=('Arial', 12),
    width=15
)


button_chuyen = tk.Button(
    root, 
    text="Chuyển", 
    font=('Arial', 12, 'bold'),
    command=convert_gregorian_to_lunar 
)


label_am = tk.Label(
    root, 
    text="Năm âm:", 
    bg=BACKGROUND_COLOR, # Đặt nền vàng
    font=('Arial', 12)
)


label_ketqua = tk.Label(
    root, 
    text="", 
    bg=BACKGROUND_COLOR, # Đặt nền vàng
    font=('Arial', 12, 'bold')
)


label_duong.place(x=30, y=30)
entry_duong.place(x=180, y=30)


button_chuyen.place(x=200, y=70)

label_am.place(x=30, y=120)
label_ketqua.place(x=180, y=120)



root.mainloop()