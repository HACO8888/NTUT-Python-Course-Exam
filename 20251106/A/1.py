def rectangle_numbers(n):
    rect_numbers = []
    i = 1
    while True:
        rect_num = i * (i + 1)
        if rect_num < n:
            rect_numbers.append(rect_num)
            i += 1
        else:
            break
    return rect_numbers

num = int(input("Enter a number n: "))
result = rectangle_numbers(num)

print("\nCalculations:")
for i, rect_num in enumerate(result, 1):
    print(f"{rect_num} = {i} × {i + 1}")