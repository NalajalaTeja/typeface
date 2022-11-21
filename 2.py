str1=input()
str2=input()
ch=str2[len(str)-1]
count=0
for i in str1:
    if i == ch:
        count+=1
print(count)