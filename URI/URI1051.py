salario = float(input())
if salario>0 and salario<=2000: print("Isento")
elif(salario>2000 and salario<=3000):
    resto = salario-2000
    result = resto*0.08
    print(f"R$ {result:.2f}")
elif(salario>3000 and salario<4500):
    resto = salario - 3000
    result = (resto * 0.18) + (1000*0.08)
    print(f"R$ {result:.2f}")
else:
    resto = salario - 4500
    result = (resto*0.28) +(1500*0.18)+(1000*0.08)
    print(f"R$ {result:.2f}")