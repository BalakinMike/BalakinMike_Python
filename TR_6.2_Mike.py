s=input()
d=[]
ds={}
dn={}
n=0
for i in s: #формируем список букв слова
  d.append(i)
#print(d)
L=(len(d)) # узнаём длину списка
#print(L)
while (n<L): #формируем словарь (буква: число вхождений)
  ds[d[n]]=d.count(d[n])
  #ds[d.count(d[n])]=d[n]
  #print(d[n], d.count(d[n]))
  n=n+1
#print(ds)  

res_dict=dict(sorted(ds.items(), key=lambda item: (-item[1], item[0])))
#print(res_dict)
k=list(res_dict.keys())
print (k)
for i in k:
  print('{0} {1}'.format(i,res_dict[i]))
  
