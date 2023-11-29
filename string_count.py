# str = "aasdddcccc"
#
# d ={}
#
# for i in str:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
#
# for itr in range(26):
#     d[chr(97+itr)] = 0
#
# for itr in str:
#     if itr in d:
#         d[itr] += 1

# str = "sdsaddmathan"
# fnd = "mathan"
# ans = 6
# ans = -1

str = "sdsaddaaamathanasdsad"
fnd = "mathan"

out = -1

for idx,itr in enumerate(str):
    if itr == fnd[0]:
        if str[idx:idx+len(fnd)] == fnd:
            out = idx

print(out)


