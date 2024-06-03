import math

# def bai_9(number, number_of_meaningful_number):
#     if number == 0:
#         return number
#     else:
#         return round(number, number_of_meaningful_number - int(math.floor(math.log10(abs(number)))) - 1)

def bai_9(number, number_of_meaningful_number):
    if number == 0:
        return number
    else:
        # Tính số lượng chữ số cần giữ lại
        num_digits = number_of_meaningful_number - int(math.floor(math.log10(abs(number)))) - 1
        
        # Chuyển đổi số thành chuỗi với độ chính xác cao hơn một chữ số để kiểm tra chữ số cuối cùng
        str_num = f"{number:.{num_digits+1}f}"
        
        # Tách phần nguyên và phần thập phân
        integer_part, fractional_part = str_num.split('.')
        
        # Kiểm tra trường hợp chữ số sau cùng là 5
        if len(fractional_part) > num_digits and fractional_part[num_digits] == '5':
            if int(fractional_part[num_digits-1]) % 2 != 0:  # Nếu chữ số trước đó là số lẻ
                rounded_number = round(number + 10**(-num_digits), num_digits)
            else:  # Nếu chữ số trước đó là số chẵn
                rounded_number = round(number, num_digits)
                fractional_part = fractional_part[:num_digits]
                rounded_number = float(f"{integer_part}.{fractional_part}")
        else:
            rounded_number = round(number, num_digits)
        
        return rounded_number

bai9 = [0.0037450, 0.004855, 0.13689, 0.23224, 0.004845]
for i in bai9:
    print(bai_9(i, 3))
