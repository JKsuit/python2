n=int(input())
list=[]
for a in range(2,n+1):
  for b in range(2,n+1):
    if a%b == 0 and a != b:
      break 
    elif a==b:
       list.append(a)

print(max(list))
    
