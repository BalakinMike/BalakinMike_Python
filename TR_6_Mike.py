s=input()
d=[]
ds={}
dn={}
n=0
for i in s:
  d.append(i)
print(d)
L=(len(d))
#print(L)
while (n<L):
  ds[d[n]]=d.count(d[n])
  #ds[d.count(d[n])]=d[n]
  print(d[n], d.count(d[n]))
  n=n+1
print(ds)  
k=list(ds.keys())
print(k)
k.sort()
dss=ds.copy()
print(dss)
print(k, len(ds))
for i in k:
    dn[i]=0
    for n in k:
        if dss[n]>dss[i]:
            dn[i]=dss[n]
            dss.pop(n)

for i in k:
  print('{0} {1}'.format(i,dn[i]))
  
