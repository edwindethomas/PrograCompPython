a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
triangle = (a*c)/2
circle = 3.14159*c*c
trapecio = ((a+b)/2)*c
square = b*b
rectangle = a*b
print(f"TRIANGULO: {triangle:.3f}\nCIRCULO: {circle:.3f}\nTRAPEZIO: {trapecio:.3f}\nQUADRADO: {square:.3f}\nRETANGULO: {rectangle:.3f}")