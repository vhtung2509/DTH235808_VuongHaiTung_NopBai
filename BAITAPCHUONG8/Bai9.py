import tkinter as tk

def calculate_bmi():
    """
    Hàm này được gọi khi nhấn nút "Tính BMI".
    Nó lấy dữ liệu, tính toán, và cập nhật các ô kết quả.
    """
    try:
        # 1. Lấy dữ liệu từ ô nhập
        height_str = entry_height.get()
        weight_str = entry_weight.get()

        if not height_str or not weight_str:
            bmi_var.set("Lỗi")
            status_var.set("Thiếu dữ liệu")
            risk_var.set("Thiếu dữ liệu")
            return

        height_m = float(height_str)  # Chuyển chiều cao sang số
        weight_kg = float(weight_str) # Chuyển cân nặng sang số

        if height_m <= 0 or weight_kg <= 0:
            raise ValueError("Dữ liệu phải > 0")

        # 2. Tính toán BMI: BMI = Cân nặng (kg) / (Chiều cao (m) * Chiều cao (m))
        bmi_value = weight_kg / (height_m * height_m)
        
        # Cập nhật ô BMI, làm tròn 1 chữ số thập phân
        bmi_var.set(f"{bmi_value:.1f}") 

        # 3. Phân loại Tình trạng và Nguy cơ
        status = ""
        risk = ""

        if bmi_value < 18.5:
            status = "Gầy / Dưới cân"
            risk = "Thấp"
        elif 18.5 <= bmi_value < 25:
            status = "Bình thường"
            risk = "Trung bình"
        elif 25 <= bmi_value < 30:
            # Đây là mức "Hơi Béo" như trong ảnh
            status = "Hơi béo / Thừa cân" 
            # Đây là mức "Hơi hơi cao" như trong ảnh
            risk = "Hơi cao" 
        elif 30 <= bmi_value < 35:
            status = "Béo phì độ I"
            risk = "Cao"
        elif 35 <= bmi_value < 40:
            status = "Béo phì độ II"
            risk = "Rất cao"
        else: # bmi_value >= 40
            status = "Béo phì độ III"
            risk = "Nguy hiểm"

        # 4. Cập nhật các ô Tình trạng và Nguy cơ
        status_var.set(status)
        risk_var.set(risk)

    except ValueError:
        # Xử lý nếu người dùng nhập chữ hoặc số không hợp lệ
        bmi_var.set("Lỗi")
        status_var.set("Vui lòng nhập số!")
        risk_var.set("Vui lòng nhập số!")

# --- Cài đặt cửa sổ chính (root) ---
root = tk.Tk()
root.title("Phần mềm tính BMI")
BACKGROUND_COLOR = "#FFFF00"  
root.config(bg=BACKGROUND_COLOR)
root.geometry("420x350") # (Rộng x Cao)

bmi_var = tk.StringVar(value="x")
status_var = tk.StringVar(value="Chưa cập nhật")
risk_var = tk.StringVar(value="Chưa cập nhật")

# --- Tạo các widget (thành phần giao diện) ---


label_height = tk.Label(root, text="Nhập chiều cao:", bg=BACKGROUND_COLOR, font=('Arial', 12))
label_weight = tk.Label(root, text="Nhập cân nặng:", bg=BACKGROUND_COLOR, font=('Arial', 12))
label_bmi_text = tk.Label(root, text="BMI của bạn:", bg=BACKGROUND_COLOR, font=('Arial', 12))
label_status_text = tk.Label(root, text="Tình trạng của bạn:", bg=BACKGROUND_COLOR, font=('Arial', 12))
label_risk_text = tk.Label(root, text="Nguy cơ phát triển bệnh:", bg=BACKGROUND_COLOR, font=('Arial', 12))



entry_height = tk.Entry(root, font=('Arial', 12), width=18)



entry_weight = tk.Entry(root, font=('Arial', 12), width=18)



entry_bmi = tk.Entry(
    root, 
    textvariable=bmi_var, 
    state="readonly", 
    readonlybackground="white",
    fg="black", 
    font=('Arial', 12, 'bold'), 
    width=18
)


entry_status = tk.Entry(
    root, 
    textvariable=status_var, 
    state="readonly", 
    readonlybackground="white", 
    fg="red", 
    font=('Arial', 12, 'bold'), 
    width=18
)

entry_risk = tk.Entry(
    root, 
    textvariable=risk_var, 
    state="readonly", 
    readonlybackground="white", 
    fg="red", 
    font=('Arial', 12, 'bold'), 
    width=18
)

# --- Các nút bấm ---

button_calc = tk.Button(
    root, 
    text="Tính BMI", 
    font=('Arial', 12, 'bold'),
    command=calculate_bmi 
)


button_exit = tk.Button(
    root, 
    text="Thoát", 
    font=('Arial', 12, 'bold'),
    command=root.destroy 
)


# Cột 1 (Nhãn)
label_height.place(x=20, y=30)
label_weight.place(x=20, y=70)
label_bmi_text.place(x=20, y=160)
label_status_text.place(x=20, y=200)
label_risk_text.place(x=20, y=240)

entry_height.place(x=200, y=30)
entry_weight.place(x=200, y=70)
entry_bmi.place(x=200, y=160)
entry_status.place(x=200, y=200)
entry_risk.place(x=200, y=240)


button_calc.place(x=240, y=110) 
button_exit.place(x=245, y=290)


root.mainloop()