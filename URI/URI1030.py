from collections import deque
def joseph(n,k):
    d = deque(n)
    while len(d)>1:
        d.rotate(-k)
        d.pop()
    return(d.pop())

nc = int(input())
for i in range(nc):
    n,k = map(int,input().split())
    n = [j for j in range(1,n+1)]
    k = int(k)
    print(f"Case {i+1}: {joseph(n,k)}")
 
