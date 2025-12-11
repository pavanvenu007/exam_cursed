p = input("Password : ")
d = u = s = 0
[(d := 1) if '0' <= x <= '9' else [(u := 1) if 'A' <= x <= 'Z' else [(s := 1) if x in "!@#$%^&*./" else None]] for x in p]
print("Valid" if (len(p) >= 8 and d and u and s) else "Invalid")