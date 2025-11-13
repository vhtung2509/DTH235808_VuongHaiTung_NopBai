import tkinter as tk

def convert_f_to_c():
    """
    Lấy giá trị độ F từ ô 'entry_f',
    tính toán độ C và cập nhật kết quả vào 'label_c_result'.
    """
    try:
        # 1. Lấy chuỗi (string) từ ô nhập liệu
        f_str = entry_f.get()
        
        # Kiểm tra nếu ô nhập liệu rỗng
        if not f_str:
            label_c_result.config(text="Chưa nhập!")
            return

        # 2. Chuyển chuỗi sang số (float)
        f_val = float(f_str)

        # 3. Áp dụng công thức chuyển đổi
        # C = (F - 32) * 5 / 9
        c_val = (f_val - 32) * 5 / 9

        # 4. Cập nhật kết quả lên nhãn
        # Dùng :.2f để làm tròn kết quả đến 2 chữ số thập phân
        label_c_result.config(text=f"{c_val:.2f} °C")

    except ValueError:
        # Xử lý nếu người dùng nhập không phải là số (ví dụ: "abc")
        label_c_result.config(text="Vui lòng nhập số!")
    except Exception as e:
        label_c_result.config(text=f"Lỗi: {e}")

# --- Cài đặt cửa sổ chính (root) ---
root = tk.Tk()
root.title("Chuyển Độ F sang Độ C")
root.geometry("350x200") # (Rộng x Cao)


BACKGROUND_COLOR = "#FFFF00" 
root.config(bg=BACKGROUND_COLOR)

# --- Tạo các widget (thành phần giao diện) ---


label_f = tk.Label(
    root, 
    text="Nhập độ F", 
    bg=BACKGROUND_COLOR, 
    font=('Arial', 12)
)

entry_f = tk.Entry(
    root, 
    font=('Arial', 12, 'bold'), 
    width=14
)


# 3. Nút "Chuyển"
button_chuyen = tk.Button(
    root, 
    text="Chuyển", 
    font=('Arial', 12, 'bold'),
    command=convert_f_to_c 
)


label_c_text = tk.Label(
    root, 
    text="Độ C", 
    bg=BACKGROUND_COLOR,
    font=('Arial', 12)
)


label_c_result = tk.Label(
    root, 
    text="Độ C ở đây", 
    bg=BACKGROUND_COLOR,
    font=('Arial', 12, 'bold')
)


label_f.place(x=30, y=30)
entry_f.place(x=150, y=30)


button_chuyen.place(x=170, y=70)

label_c_text.place(x=30, y=120)
label_c_result.place(x=150, y=120)


root.mainloop()