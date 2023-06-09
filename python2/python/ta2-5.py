in_txt = input()

in_int_txt = int(in_txt) - 1

first = 0
second = 1

if in_int_txt == 0:
    print(0)
elif in_int_txt == 1:
    print(1)
else:
    i = 0

    while i < in_int_txt - 1:
        first, second = second, first + second
        i += 1

    print(second)