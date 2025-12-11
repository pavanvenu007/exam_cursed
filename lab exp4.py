students={
"Pavan   ":[("Java",85),("Python",78),("DBMS",91),("AI",88),("PST",73)],
"Venu    ":[("Java",67),("Python",72),("DBMS",69),("AI",75),("PST",80)],
"Aradhya ":[("Java",90),("Python",94),("DBMS",89),("AI",92),("PST",88)],
"Musharaf":[("Java",50),("Python",61),("DBMS",55),("AI",58),("PST",63)],
"Manoj   ":[("Java",77),("Python",83),("DBMS",81),("AI",79),("PST",75)]
}

[(lambda n,m,t,p,g:print(n,"\t =>",m,"\t | Total:",t,"\t | %:",p,"\t | Grade:",g))(n,m,sum(x[1] for x in m),
(sum(x[1] for x in m))/len(m),
(lambda x:"O"if x>=90 else"A"if x>=80 else"B"if x>=70 else"C"if x>=60 else"F")
((sum(x[1] for x in m))/len(m))) for n,m in students.items()]
