import numpy as np
from sklearn.linear_model import LinearRegression

# --- 1. Chuẩn bị dữ liệu từ bảng ---
# Dữ liệu Chiều cao (cm) - Đây là biến độc lập (X)
X_data = [
    147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183
]

# Dữ liệu Cân nặng (kg) - Đây là biến phụ thuộc (y)
y_data = [
    49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68
]

# --- 2. Định dạng lại dữ liệu ---
# Scikit-learn yêu cầu mảng X phải là mảng 2 chiều (nhiều hàng, 1 cột)
# Chúng ta dùng numpy.array() và .reshape(-1, 1)
X = np.array(X_data).reshape(-1, 1)

# mảng y có thể là 1 chiều
y = np.array(y_data)

# --- 3. Xây dựng và Huấn luyện (train) mô hình ---
print("Đang huấn luyện mô hình...")

# Khởi tạo mô hình Hồi quy tuyến tính
model = LinearRegression()

# "Fit" (huấn luyện) mô hình với dữ liệu X và y
model.fit(X, y)

print("Đã huấn luyện xong!")

# --- 4. Lấy thông tin từ người dùng ---
print("-" * 30)
try:
    # Yêu cầu người dùng nhập chiều cao
    user_height_str = input("Nhập chiều cao của bạn (cm): ")
    
    # Chuyển đổi sang số (float)
    user_height = float(user_height_str)

    # --- 5. Chuẩn bị dữ liệu của người dùng để dự đoán ---
    # Dữ liệu dự đoán cũng phải là mảng 2 chiều
    # Ví dụ: nếu người dùng nhập 170, nó phải là [[170]]
    user_height_2d = np.array([[user_height]])

    # --- 6. Thực hiện dự đoán ---
    predicted_weight = model.predict(user_height_2d)

    # --- 7. In kết quả ---
    # predicted_weight là một mảng (ví dụ [62.5]), nên ta lấy phần tử đầu tiên
    print(f"\n>> Chiều cao: {user_height} cm")
    print(f">> Cân nặng dự đoán: {predicted_weight[0]:.2f} kg") # Làm tròn 2 chữ số

except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")