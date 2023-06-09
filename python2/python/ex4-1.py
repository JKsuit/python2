n = input()

a = n.split()

i = 0
answer = []
while i < len(a):
  answer.append(a[i][::-1])

  i += 1

print(" ".join(answer))