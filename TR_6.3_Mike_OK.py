s=input()
d=[]
ds={}
dn={}
n=0
for i in s: # формируем список по буквам
  d.append(i)
L=(len(d)) 
while (n<L): # формируем словарь с однократным вхождением буквы (в качестве ключа) и количеством вхождений данной буквы в качестве значения
  ds[d[n]]=d.count(d[n])
  n=n+1
# сортировка 
res_dict=dict(sorted(ds.items(), key=lambda item: (-item[1], item[0])))
k=list(res_dict.keys())
schet=1
# печать согласно требованию (первые три буквы с самым частым вхождением)
for i in k:
    if schet<4:
        print('{0} {1}'.format(i,res_dict[i]))
        schet=schet+1
    else:
        break
    
