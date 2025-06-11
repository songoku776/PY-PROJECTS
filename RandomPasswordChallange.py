# lesson 22 Random Password Challange
import random
import string

def generate_password(length=10):
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    all_chars = lowercase_letters + uppercase_letters + digits

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits)
    ]

    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    return ''.join(password)
print("Your random password is:", generate_password())
