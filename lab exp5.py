# COMPLEX GRAPH + EXTREME CURSED DFS
graph={'A':['B','C','D'],'B':['E','F'],'C':['G'],'D':['H','I'],'E':[],'F':['J'],'G':['E','I'],'H':['C'],'I':['J'],'J':[]}
v=set();r=[]
dfs=lambda n:(r.append(n),v.add(n),[dfs(x) for x in graph[n] if x not in v])
dfs('A')
print("DFS Traversal:",r)