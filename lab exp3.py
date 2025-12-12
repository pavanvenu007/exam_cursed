#1st
lst=[10,20,20,30,80,10,50,89,70]

s=0;[s:=s+x for x in lst]
print("Mean:",s/len(lst))

for _ in lst:[(lst.__setitem__(j,(lst[j+1],lst.__setitem__(j+1,lst[j]))[0])) for j in range(len(lst)-1) if lst[j]>lst[j+1]]
print("Sorted:",lst)

m=len(lst)//2;print("Median:",(lst[m] if len(lst)%2 else (lst[m]+lst[m-1])/2))

d={};[d.__setitem__(x,d.get(x,0)+1) for x in lst]
mx=(lambda v:[(v:=d[i]) for i in d if d[i]>v] and v)(0)
print("Mode:",[i for i in d if d[i]==mx])

mx=mn=lst[0];[(mx:=x if x>mx else mx, mn:=x if x<mn else mn) for x in lst]
print("Max:",mx,"Min:",mn)

u=[x for i,x in enumerate(lst) if x not in lst[:i]]
print("Unique:",u)

#2nd
import statistics as s

lst = [10,20,20,30,80,10,50,89,70]

print("mean : ", s.mean(lst))
print("median : ", s.median(lst))
print("mode : ", s.mode(lst))
print("sorted : ", sorted(lst))
print("unique : ", set(lst))
print("max : ", max(lst))
print("min : ", min(lst))