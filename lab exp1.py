n = int(input("enter no. : "))
f = lambda s, x, i : (print(i), s(s, x // i, i)) if x % i == 0 else (s(s, x, i + 1) if i <= x else None)
f(f, n, 2)