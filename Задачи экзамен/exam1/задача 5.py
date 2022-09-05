#Задача 5
m = 1
n = 50
if m<n:
    for i in range(m,n+1):
        print(i)
elif m>n:
    for i in range(m,n-1,-1):
        print(i)