a=input()
list=[]
for i in a[::-1]:
   if i not in list:
      list.append(i)
print(''.join(list[::-1]))