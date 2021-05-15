some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx, some in enumerate(some_list):
    if some.replace("-", "").replace("+", "").isdigit():
        add_digit = ""
        if not some[0].isdigit():
            add_digit = some[0]
        some_list[idx] = f'"{add_digit}{int(some):02}"'

print(" ".join(some_list))
