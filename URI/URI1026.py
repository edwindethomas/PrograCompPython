try:
    while True:
        dato1,dato2 = map(int,input().split())
        print(f"{dato1^dato2}")
except EOFError:
    pass