import math

def bai_9(number, number_of_meaningful_number):
    if number == 0:
        return number
    else:
        return round(number, number_of_meaningful_number - int(math.floor(math.log10(abs(number)))) - 1)
    
bai9 = [0.0037450, 0.004855, 0.13689, 0.23224]
for i in bai9:
    print(bai_9(i, 3))