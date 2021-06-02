src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_new = {src_: 0 for src_ in src}
for src_ in src:
    if src_ in src_new:
        src_new[src_] += 1
print(src_new)

src_new = [src_ for src_ in src_new if src_new[src_] == 1]
print(src_new)
