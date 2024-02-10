prod = 1
my_list=list(map(int,input().split()))
for i in my_list:
    prod=prod*i
    
lst=[]
for i in my_list:
    lst.append(prod//i)
print(lst)
