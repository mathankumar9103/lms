# n = 15
# end_value = 10
# for i in range(1,end_value + 1,1):
#     print(n,"*",i,"=",n*i)

#string_replace

# string = "programmer"
# fin = 'o'
# rpl = '#'
# new_str = ""
# for i in string:
#     if i == fin:
#         new_str += rpl
#     else:
#         new_str += i
# print(new_str)

#String_split

# str_a = "I am a programmer"
# var = 'm'
# res = ""
# lst = []
# for i in str_a:
#     if i != var:
#         res += i
#     else:
#         lst.append(res)
#         res = ""
# if res:
#     lst.append(res)
#     print(lst)

#string_join

# lst = ["I","am","a","programmer"]
# res = ""
# for i in lst:
#     if i != lst[-1]:
#         res += i + '#'
#     else:
#         res += i
# print(res)

#string_index

# str = "programmer"
# str_find = "a"
# for idx,item in enumerate(str):
#     if item == str_find:
#         print(idx+1)


# str = ["I","am","trying","to","become","programmer"]
# res = ""
# str_join = "-"
# for i in str:
#     if i != str[-1]:
#         res += i + str_join
#     else:
#         res += i
# print(res)

#string_count

# str = "practice makes the man perfect"
# str_count = "a"
# count = 0
# for i in str:
#     if i == str_count:
#         count += 1
# print(count)

#string_endswith

# str = "Hey,We welcomes you."
# search = "."
# if str[-1] == search:
#     print(True)
# else:
#     print(False)

#str_starswith

# str = "Hey,We welcomes you."
# search = "H"
# if str[-1] == search:
#     print(True)
# else:
#     print(False)

#string_title

str = "welcome to the programming word"
print(str.title())
