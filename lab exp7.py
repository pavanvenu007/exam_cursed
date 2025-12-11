S=(0,0);G=(3,3)
O=[S];C=set();P={S:None};Gm={S:0}
H=lambda a,b:abs(a[0]-b[0])+abs(a[1]-b[1])
N=lambda x:[(x[0]+1,x[1]),(x[0]-1,x[1]),(x[0],x[1]+1),(x[0],x[1]-1)]
V=lambda x:0<=x[0]<4 and 0<=x[1]<4

while O:
    n=min(O,key=lambda x:Gm[x]+H(x,G))
    if n==G:break
    O.remove(n);C.add(n)
    for k in N(n):
        if V(k) and k not in C and (k not in O or Gm[k]>(Gm[n]+1)):
            k not in O and O.append(k)
            P.__setitem__(k,n);Gm.__setitem__(k,Gm[n]+1)

r=[];x=G
while x!=None:r+=[x];x=P[x]
print(r[::-1])
