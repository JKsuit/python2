year=(int(input()))
if year%4!=0:
  print("a normal year")
elif year%4==0 and year%100!=0:
  print("a leap year")
elif year%100==0 and year%400!=0:
  print("a normal year")
elif year%400==0:
  print("a leap year")