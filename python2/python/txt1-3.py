

in_txt = input()

in_list = in_txt.split()

noopen = ['星期五', '星期六', '星期日']

if in_list[0] in noopen:
    print('不開市')
else:
    print(int(in_list[1]) * int(in_list[2]))