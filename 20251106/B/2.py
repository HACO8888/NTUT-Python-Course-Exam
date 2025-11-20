def count_digits(n):
    digit_count = [0] * 10 

    while n > 0:
        digit = n % 10
        digit_count[digit] += 1 
        n //= 10

    for digit in range(10):
        if digit_count[digit] > 0:
            times = "time" if digit_count[digit] == 1 else "times"
            print(f"Digit {digit} appears {digit_count[digit]} {times}")
            
n = int(input("Enter a positive integer: "))
count_digits(n)