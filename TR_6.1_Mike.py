s=input()
d=[]
ds={}
dn={}
n=0
for i in s: #формируем список букв слова
  d.append(i)
print(d)
L=(len(d)) # узнаём длину списка
#print(L)
while (n<L): #формируем словарь (буква: число вхождений)
  ds[d[n]]=d.count(d[n])
  #ds[d.count(d[n])]=d[n]
  #print(d[n], d.count(d[n]))
  n=n+1
print(ds)  
k=list(ds.keys())
print(k)
k.sort()
print(k)
dss=ds.copy()

for i in k:
  print('{0} {1}'.format(i,ds[i]))
  
