rules=[
    ("sunny",lambda t,h,w:t>25 and h<60 and w=="low"),
    ("hot",lambda t,h,w:t>30 and h>60),
    ("humid",lambda t,h,w:h>80),
    ("windy",lambda t,h,w:w=="high"),
    ("rainy",lambda t,h,w:h>70 and w=="medium"),
    ("cold",lambda t,h,w:t<15)
]

classify=lambda t,h,w:next((r for r,f in rules if f(t,h,w)),"unknown")

t,h,w=input("t h w: ").split()
print(classify(int(t),int(h),w))
