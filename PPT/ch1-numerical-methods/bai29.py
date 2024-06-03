import math

# Giá trị thực của pi
pi_real = 3.14159265358979

# Xấp xỉ 1 và 2
approx_1 = 22 / 7
approx_2 = 355 / 113

# Tính lỗi tuyệt đối
absolute_error_1 = abs(approx_1 - pi_real)
absolute_error_2 = abs(approx_2 - pi_real)

# Tính lỗi tương đối
relative_error_1 = absolute_error_1 / pi_real
relative_error_2 = absolute_error_2 / pi_real

# Làm tròn đến 14 chữ số có nghĩa
absolute_error_1 = round(absolute_error_1, 14)
absolute_error_2 = round(absolute_error_2, 14)
relative_error_1 = round(relative_error_1, 14)
relative_error_2 = round(relative_error_2, 14)

# Kết quả
print((absolute_error_1, f"{relative_error_1*100} %"), (absolute_error_2, f"{relative_error_2 * 100} %"))
