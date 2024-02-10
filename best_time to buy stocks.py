
hip=0
lst=[7,1,3,5,6,20,0]
for i in range (len(lst)-1):
    if max(lst[i+1:])-lst[i] >hip:
        hip=max(lst[i+1:])-lst[i]
print (hip)
