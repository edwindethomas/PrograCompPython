while (True) :
    h1,m1,h2,m2 = map(int,input().split())
    if(h1==0 and m1==0 and h2==0 and m2==0): break
    else:
        hm1 = h1 *60
        total1 = hm1+m1
        hm2 = h2 *60
        total2 = hm2+m2
        if total1<=total2:
            print(f"{total2-total1}")
        else:
            total1 = 1440-total1
            print(f"{total2+total1}")