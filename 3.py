n=int(input("enter: "))
x=0
c=1
while(n):
    if '3' in str(c) or '7' in str(c) or '4' in str(c):
        c+=1
        continue
    if '2' in str(c) or '5' in str(c) or '6' in str(c) or '9' in str(c) or '0' in str(c) or '1' in str(c) or '8' in str(c):
        n-=1
        x=c
    c+=1
print(x)