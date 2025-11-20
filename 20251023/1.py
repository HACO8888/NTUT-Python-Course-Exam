def is_armstrong(n):
    digits = str(n)
    length = len(digits)
    ans_sum = sum(int(digit) ** length for digit in digits)

    return ans_sum == n
  
n=int(input("Enter a number: "))
print(is_armstrong(n))