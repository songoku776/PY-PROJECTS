# lesson 21 List Comprehension Projetc
num = int(input("Enter a number: "))

odd_numbers_under = [i for i in range(num) if i % 2 != 0]

odd_numbers_upto_double = [i for i in range(num * 2) if i % 2 != 0]

print("Odd numbers under", num, ":", odd_numbers_under)
print("Odd numbers up to 2 ×", num, ":", odd_numbers_upto_double)

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Capitalized fruits list:", capitalized_fruits)
