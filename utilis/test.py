def find_two_squares(n):
    for a in range(int(n**0.5) + 1):
        b_squared = n - a**2
        b = int(b_squared**0.5)
        if a**2 + b**2 == n:
            return (a, b)
    return None

result = find_two_squares(25)
print(result)