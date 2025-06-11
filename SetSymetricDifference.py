# lesson 20 Set Symetric Difference project
start_num = int(input("enter the starting number: "))
end_num = int(input("enter the ending number: "))

squared_numbers = []
for num in range(start_num, end_num + 1):
    squared_numbers.append(num * num)

print("\nAll squared numbers:", squared_numbers)

odd_squares = []
even_squares = []

for square in squared_numbers:
    if square % 2 == 0:  
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Odd squared numbers:", odd_squares)
print("Even squared numbers:", even_squares)
