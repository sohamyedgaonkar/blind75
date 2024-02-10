ans=[]
lst=[1,3,7,5]
target=10
for i in range (len(lst)):
    for j in range (i+1,len(lst)):
        if lst[i]+lst[j]== target:
            ans.append(i)
            ans.append(j)
print (ans)
