def compare(num_1, num_2):
    if num_1 > num_2:
        return f"{num_1} is greater than {num_2}"
    elif num_1 < num_2:
        return f"{num_1} is less than {num_2}"
    else:
        return f"{num_1} is equal to {num_2}"

def can_divide_by(num_1, num_2):
    return num_1 % num_2 == 0

def password_length(password):
    return len(password)

def password_includes_special_chars(password):
    special_chars = [".", "!", "£", "$", "%", "&", "*"]
    for char in password:
        for special_char in special_chars:
            if char == special_char:
                return True

def password_includes_upper_char(password):
    for char in password:
        if char == char.upper():
            return True

def password_acceptable(password):
    if password_length(password) > 8 and password_includes_special_chars(password) and password_includes_upper_char(password):
        return True