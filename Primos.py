n = 500
p = [2] + [x for x in range(3, n+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if (float(x) / y).is_integer()]]
print(p)
