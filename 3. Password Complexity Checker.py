def check_password_complexity(password):
    upper_chars = lower_chars = digits = special_chars = 0
    length = len(password)
    
    if length < 6:
        print("Password must be at least 6 characters long!")
        return
    
    for char in password:
        if char.isupper():
            upper_chars += 1
        elif char.islower():
            lower_chars += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1
    
    if upper_chars and lower_chars and digits and special_chars:
        if length >= 10:
            print("Password strength: Strong")
        else:
            print("Password strength: Medium")
    else:
        if not upper_chars:
            print("Password must contain at least one uppercase character!")
        if not lower_chars:
            print("Password must contain at least one lowercase character!")
        if not digits:
            print("Password must contain at least one digit!")
        if not special_chars:
            print("Password must contain at least one special character!")

password = input("Enter your password: ")
check_password_complexity(password)
