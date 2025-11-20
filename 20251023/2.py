def reverse_number(n):
    rnum = 0
    onum = n

    while n > 0:
        digit = n % 10
        rnum = rnum * 10 + digit
        n //= 10

    return rnum == onum

n = int(input("Enter a number: "))
print(reverse_number(n))

