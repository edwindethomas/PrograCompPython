t = int(input())
index = 0
dic= {}
while index<t:
    n = int(input())
    if n in dic:
        dic[n] = dic.get(n)+1
    else:
        dic[n] =1
    index +=1
sort_dic = sorted(dic)
for i in sort_dic:
    print(f"{i} aparece {dic[i]} vez(es)")