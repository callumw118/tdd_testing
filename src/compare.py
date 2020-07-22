def compare(num_1, num_2):
    if num_1 > num_2:
        return f"{num_1} is greater than {num_2}"
    elif num_1 < num_2:
        return f"{num_1} is less than {num_2}"
    else:
        return f"{num_1} is equal to {num_2}"

def can_divide_by(num_1, num_2):
    return num_1 % num_2 == 0