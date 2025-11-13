import tkinter as tk

class Calculator:
    def __init__(self, master):
        """Hàm khởi tạo (constructor) của lớp Calculator."""
        self.master = master
        master.title("Máy tính Tkinter")
        master.geometry("350x450") # Đặt kích thước cửa sổ cố định
        
        # Biến trạng thái
        self.first_num = 0
        self.operation = ""
        # Cờ (flag) này kiểm tra xem có nên xóa màn hình
        # khi người dùng bấm số mới (sau khi bấm 1 phép toán)
        self.new_number_started = True

        # Màn hình hiển thị (Entry widget)
        self.display = tk.Entry(master, 
                                font=('Arial', 24), # Font chữ to
                                borderwidth=5,      # Viền
                                justify="right")    # Căn lề phải
        
        # Đặt màn hình vào lưới (grid)
        # sticky="nsew" làm cho widget co giãn theo 4 hướng
        # columnspan=4 nghĩa là nó chiếm 4 cột
        self.display.grid(row=0, column=0, columnspan=4, 
                          padx=10, pady=10, sticky="nsew")

        # --- Tạo các nút bấm ---
        
        # Danh sách các nút
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
        ]

        # Vòng lặp để tạo và định vị các nút
        row_val = 1
        col_val = 0
        for text in buttons:
            cmd = None # Lệnh (command) cho nút
            
            # Gán lệnh (command) tương ứng cho từng loại nút
            if text == 'C':
                cmd = self.on_clear
            elif text in ['/', '*', '-', '+']:
                # Dùng lambda để truyền tham số (phép toán) vào hàm
                cmd = lambda op=text: self.on_operation(op)
            else:
                # Dùng lambda để truyền tham số (chữ số) vào hàm
                cmd = lambda num=text: self.on_digit(num)

            # Tạo nút
            btn = tk.Button(master, text=text, 
                            font=('Arial', 18), 
                            command=cmd)
            
            # Đặt nút vào lưới
            btn.grid(row=row_val, column=col_val, 
                     sticky="nsew", padx=5, pady=5)

            # Di chuyển vị trí cột
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Nút " = " (đặt riêng vì nó chiếm 4 cột)
        btn_equal = tk.Button(master, text="=", 
                              font=('Arial', 18), 
                              command=self.on_equal)
        btn_equal.grid(row=5, column=0, columnspan=4, 
                       sticky="nsew", padx=5, pady=5)

        # --- Cấu hình co giãn cho lưới (Grid) ---
        # Cho phép các hàng và cột co giãn khi thay đổi kích thước cửa sổ
        
        # Cột 0-3 (4 cột)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        
        # Hàng 0 (màn hình)
        master.grid_rowconfigure(0, weight=1) 
        # Hàng 1-5 (các nút)
        for i in range(1, 6):
            master.grid_rowconfigure(i, weight=2) # Nút co giãn nhiều hơn

    # --- Các phương thức xử lý logic ---

    def on_digit(self, digit):
        """Xử lý khi người dùng bấm số (0-9) hoặc dấu chấm (.)."""
        # Nếu đây là số mới (sau một phép toán), hãy xóa màn hình
        if self.new_number_started:
            self.display.delete(0, tk.END)
            self.new_number_started = False
            
        current = self.display.get()
        
        # Ngăn người dùng nhập nhiều hơn 1 dấu chấm
        if digit == '.' and '.' in current:
            return 
            
        self.display.insert(tk.END, digit)

    def on_clear(self):
        """Xử lý khi người dùng bấm nút 'C' (Clear)."""
        self.display.delete(0, tk.END)
        self.first_num = 0
        self.operation = ""
        self.new_number_started = True

    def on_operation(self, op):
        """Xử lý khi người dùng bấm phép toán (+, -, *, /)."""
        try:
            # Lưu số hiện tại trên màn hình
            self.first_num = float(self.display.get())
        except ValueError:
            # Nếu màn hình rỗng, coi như là số 0
            self.first_num = 0
        
        self.operation = op # Lưu phép toán
        self.new_number_started = True # Đánh dấu để chuẩn bị nhập số mới

    def on_equal(self):
        """Xử lý khi người dùng bấm nút '='."""
        # Nếu không có phép toán nào, thì không làm gì cả
        if self.operation == "":
            return

        try:
            # Lấy số thứ hai từ màn hình
            second_num = float(self.display.get())
        except ValueError:
            # Nếu người dùng bấm "=" khi chưa nhập số thứ 2
            self.on_clear()
            self.display.insert(0, "Lỗi")
            return

        result = 0
        try:
            # Thực hiện phép tính
            if self.operation == "+":
                result = self.first_num + second_num
            elif self.operation == "-":
                result = self.first_num - second_num
            elif self.operation == "*":
                result = self.first_num * second_num
            elif self.operation == "/":
                result = self.first_num / second_num
        except ZeroDivisionError:
            # Xử lý lỗi chia cho 0
            self.on_clear()
            self.display.insert(0, "Lỗi chia 0")
            return

        # --- Hiển thị kết quả ---
        self.display.delete(0, tk.END)
        
        # Hiển thị số nguyên nếu kết quả là số nguyên (ví dụ: 5.0 -> 5)
        if result.is_integer():
            self.display.insert(0, int(result))
        else:
            # Giữ lại số thập phân nếu cần
            self.display.insert(0, str(result))
        
        # Đặt lại trạng thái
        self.operation = ""
        self.new_number_started = True

# --- Phần chính để chạy ứng dụng ---
if __name__ == "__main__":
    root = tk.Tk()           # Tạo cửa sổ chính
    my_calculator = Calculator(root) # Tạo một đối tượng Calculator
    root.mainloop()          # Chạy vòng lặp sự kiện của Tkinter