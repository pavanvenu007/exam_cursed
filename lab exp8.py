t={'A':{'B':{'D':{10,3},'E':{7,4}},
        'C':{'F':{8,4},'G':{17,1}}}}

minimax=lambda n,tr,mx: (
    (v:=( [minimax(c,tr[n],not mx) for c in tr[n]] ),
     m:=max(v,key=lambda x:x[0]) if mx else min(v,key=lambda x:x[0]),
     (m[0],[n]+m[1]) )[2]
    ) if isinstance(tr[n],dict) else (
    (max(tr[n]) if mx else min(tr[n]),[n])
    )

val,path=minimax('A',t,True)
print("Value:",val)
print("Path:","->".join(path))