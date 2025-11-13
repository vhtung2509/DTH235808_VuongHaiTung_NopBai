import tkinter as tk
from tkinter import ttk # (Tùy chọn) Sử dụng cho các widget trông "hiện đại" hơn

# --- Thiết lập cửa sổ chính ---
root = tk.Tk()
root.title("frame 2") # Đặt tiêu đề cửa sổ
root.geometry("600x300") # Đặt kích thước ban đầu (Rộng x Cao)

# --- Danh sách các style ---
# Đây là 6 loại relief (style viền) cơ bản trong tkinter
relief_styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

# --- Tạo tiêu đề cột ---
# (Phần này không có trong ảnh nhưng giúp giao diện rõ ràng hơn)
# Bạn có thể bỏ đi nếu muốn
tk.Label(root, text="Border Width", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=10, pady=10)
for j, style in enumerate(relief_styles):
    tk.Label(root, text=style, font=('Arial', 10, 'bold')).grid(row=0, column=j+1, padx=5, pady=10)


# --- Vòng lặp chính để tạo Button ---

# Vòng lặp 1: Duyệt qua các giá trị borderwidth (0, 1, 2, 3, 4)
for i in range(5):
    borderwidth_value = i
    
    # Tạo nhãn "borderwidth = i" ở cột đầu tiên
    label = tk.Label(root, text=f"borderwidth = {borderwidth_value}")
    label.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w") # (i+1) vì hàng 0 là tiêu đề
    
    # Vòng lặp 2: Duyệt qua từng style trong danh sách relief_styles
    for j, style in enumerate(relief_styles):
        
        # Tạo nút Button
        btn = tk.Button(
            root,
            text=style,
            width=10, # Đặt chiều rộng cố định cho nút
            bd=borderwidth_value,  # 'bd' là viết tắt của 'borderwidth'
            relief=style           # 'relief' chính là style của viền
        )
        
        # Đặt nút vào lưới (grid)
        # (j+1) vì cột 0 là nhãn "borderwidth = ..."
        btn.grid(row=i + 1, column=j + 1, padx=5, pady=5) 

# --- Chạy ứng dụng ---
root.mainloop()