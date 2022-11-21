def base3(num):
    if num<0:
        x='-'
    else:
        x=''
    num=abs(num)
    if num<3:
        return num
    ans=''
    while num!=0:
        ans=str(num%3)+ans
        num=num//3
    return x+ans
print(base3(10))