num= int(input())
if num > 0: 
        n = 0
        while num > 0: 
            if num % 2 == 0: 
                num //= 2
            else:
               num -= 1
                 
            n += 1
        print(n) 
else: 
        print(0)