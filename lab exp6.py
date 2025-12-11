A=int(input("A: "))
B=int(input("B: "))
T=int(input("T: "))

s=(0,0);v={s};q=[s];p={s:None};g=None

mv=lambda x,y:[(A,y),(x,B),(0,y),(x,0),
(min(A,x+y),x+y-min(A,x+y)),
(x+y-min(B,x+y),min(B,x+y))]

while q and not g:
    u=q.pop(0)
    for n in mv(*u):
        if n not in v:
            v.add(n);p[n]=u;q.append(n)
            if n[0]==T or n[1]==T:g=n;break

r=[];x=g
while x!=None:r.append(x);x=p[x]

print(r[::-1])
