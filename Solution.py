entry_list=int(map(int,input().split())
d=dict()
for i in entry_list:
  if i not in d:
     d[i]=1
  else:
     d[i]+=1
for i,j in d.items():
   print('element:',str(i), 'count:', str(j))

