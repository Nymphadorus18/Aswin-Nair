b=input()
x=list(map(str,input().split(",")))
lst=[]
for i in x:
    string=""
    for j in range(len(i)-1,-1,-1):
        string=string+i[j]
    lst.insert(len(lst),string)
print(*lst)
lst2=[]
for i in range(len(x)-1,-1,-1):
    lst2.append(x[i])
print(*lst2)