s=input()
d=[]
ds={}
n=0
for i in s:
  d.append(i)
print(d)
L=(len(d))
print(L)
#k=0
while (n<L):
  print(d[n])
  ds[d[n]]=d.count(d[n])
  #k=n 
  #while (k<L):
    #if (d(n)==d(k+1)):

    
    #k=k+1 
  #print(d[n])
  n=n+1
print(ds)  


