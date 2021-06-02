src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[i + 1] for i in range(0, len(src) - 1) if src[i + 1] > src[i]]

print(result)
