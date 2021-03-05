par = impar = pos = neg = 0
for i in range(5):
    aux = int(input())
    if(aux >= 1):pos+=1
    elif(aux<=-1):neg+=1
    if(aux%2== 0):par+=1
    else: impar+=1
print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")