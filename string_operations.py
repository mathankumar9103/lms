#remove duplicates from given string
# input str = "asfkjifllkjajkju"
# result str = "asfkjilu"

# str = "asfkjifllkjajkjuaadsahgaaaassssss"
#
# #longest commong pattern
#
# pattern_length = 0
# pattern_match = ''
#
# for itr,itr_item in enumerate(str):
#     pattern = itr_item
#     for itr1 , itr_item1 in enumerate(str[itr+1:]):
#         if itr_item == itr_item1:
#             pattern = pattern + itr_item1
#         else:
#             if pattern_length < len(pattern):
#                 pattern_length = len(pattern)
#                 pattern_match = pattern
#             break
#     if pattern_length < len(pattern):
#         pattern_length = len(pattern)
#         pattern_match = pattern
# print(pattern_match)
# print(pattern_length)







#find a word in given string

# str = "hellomathanhowareyou"
# keyword = "mathan"
#
# for i , itr in enumerate(str):
#     pattern = itr
#     for i1 , itr1 in enumerate(str[itr+1:]):
#         if itr1 == keyword:
#             keyword = itr1
# print(itr1)







# for i in keyword:
#     if i in str:
#         new = new + i
#         if new == keyword:
#             print(new)

#
# pattern_length = 0
# pattern_match = ''
# for itr,itr_item in enumerate(str):
#     pattern = itr_item
#     for itr1,itr_item1 in enumerate(str[itr+1:]):
#         if itr_item == itr_item1:
#             pattern = pattern + itr_item1
#         else:
#             if pattern_length < len(pattern):
#                 pattern_length = len(pattern)
#                 pattern_match = pattern
#             break
#
#     if pattern_length < len(pattern):
#         pattern_length = len(pattern)
#         pattern_match = pattern
#
# print(pattern_match)
# print(pattern_length)



str = "sdsaddmathanasdsad"
fnd = "mathan"

if fnd in str:
    print(True)
    ans = str.find(fnd)
else:
    print(False)
    ans = str.find(fnd)

print("starting index:",ans)