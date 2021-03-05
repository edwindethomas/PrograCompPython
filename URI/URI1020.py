dias = int(input())
anhos = dias//365
dias = dias%365
meses = dias//30
dias = dias%30
print(f"{anhos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")