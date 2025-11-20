def combination(m, n):
    if n == 0 or m == n:
        return 1
    else:
        return combination(m - 1, n) + combination(m - 1, n - 1)
      
m = int(input("Enter m: "))
n = int(input("Enter n: "))
print(f"C({m},{n}) =", combination(m, n))