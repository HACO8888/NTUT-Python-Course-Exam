def perfect_squares(n):
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
    return squares
  
n = int(input("Enter a number: "))
result = perfect_squares(n)
print("Perfect squares less than or equal to", n, "are:", result)