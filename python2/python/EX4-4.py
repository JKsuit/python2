a=input()

x=0
y=0

for i in list(a): 
  
    if i == 'U': 
            y += 1
    elif i == 'D':
            y -= 1
    elif i == 'L':
            x -= 1
    else:
            x += 1
if (x == 0 and y == 0):
        print('Y') 
else:
        print('N')           