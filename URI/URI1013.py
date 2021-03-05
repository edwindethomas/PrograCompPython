a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
maiorAB = ((a + b) + abs(a-b))//2
maiorAC = ((a + c) + abs(a-c))//2
maior = ((maiorAB + maiorAC) + abs(maiorAB-maiorAC))//2
print(f"{maior} eh o maior")