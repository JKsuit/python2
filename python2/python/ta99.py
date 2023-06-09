import sys
aa=sys.stdin.read()

for i,a in enumerate (aa.splitlines()):
  print(a,i+1,sep='')

