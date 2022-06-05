list=["my name is rafat and my age is 123456319 years old"]
i=0
c=0
c1=0
c2=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j].isdigit():
            c=c+1
        if list[i][j].lower()and list[i][j].upper():
            c1=c1+1
        else:
            c2=c2+1
        j=j+1
    i=i+1
print(c)
print(c1)
print(c2)
print(len(list))


