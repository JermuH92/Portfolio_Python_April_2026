def check_pass_length(password):
    return len(password) >= 8 

def check_has_numbers(password):
    return any(char.isdigit() for char in password)

def check_has_uppercase(password):
    return any(char.isupper() for char in password)
      
password_rules = [check_pass_length, check_has_numbers, check_has_uppercase]