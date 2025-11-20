def check_password(num):
    num_str = str(num)
    
    if len(num_str) != 4 or not num_str.isdigit():
        return "Invalid Password"
    
    if len(set(num_str)) != 4:
        return "Invalid Password"
      
    digit_sum = sum(int(digit) for digit in num_str)
    if digit_sum % 2 != 0:
        return "Invalid Password"
    
    if '0' in num_str:
        return "Invalid Password"
    
    return "Valid Password"
  
password = int(input("Enter a 4-digit password: "))
print(check_password(password))