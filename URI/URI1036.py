import math
a,b,c = input().split()
a = float(a) 
b = float(b) 
c = float(c)
discriminante = (b*b)-(4*a*c)
if(a == 0 or discriminante<=-1): print("Impossivel calcular")
else:
    discsqrt = math.sqrt(discriminante)
    res1 = ((-1*b)+discsqrt)/(2*a)
    res2 = ((-1*b)-discsqrt)/(2*a)
    print(f"R1 = {res1:.5f}")
    print(f"R2 = {res2:.5f}")