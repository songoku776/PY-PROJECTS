# lesson 8 Binary Conversion project
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_digits = []
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num = decimal_num // 2
    
    binary_num = ''.join(reversed(binary_digits))
    return binary_num

decimal_input = float(input("Enter a decimal number: "))

binary_result = decimal_to_binary(decimal_input)
print(f"The binary representation is: {binary_result}")