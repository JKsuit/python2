in_txt = input()

in_list = in_txt.split()

ans = ""

i = 0
while i < len(in_list):
    ans += str(int(in_list[i]) + 1) + ' '
    i += 1

print(ans.strip())
