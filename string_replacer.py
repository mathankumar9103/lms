str = "abcdef"
new_str = ''
present_value = input("enter the value to replace:")
replaced_value =input("enter the replacing value:")
for i in str:
    if i == present_value:
        new_str = new_str + replaced_value
    else:
        new_str = new_str + i
print(new_str)







str1 = "aasdddcccc"

d ={}

for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)