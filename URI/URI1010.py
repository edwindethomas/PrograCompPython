cod1,uni1,pre1 = input().split()
cod2,uni2,pre2 = input().split()
uni1 = int(uni1)
uni2 = int(uni2)
pre1 = float(pre1)
pre2 = float(pre2)
res = uni1*pre1 + uni2*pre2
print(f"VALOR A PAGAR: R$ {res:.2f}")