# student = "vignesh"
# student1 = "mathan"
#
# a = student.capitalize()
# b = student1.capitalize()
#
# print(a,b)
# print("{} {}".format(student.capitalize(),student1.capitalize()))
# print(student.capitalize(),student1.capitalize())

# a = "1111 ^^^^ 2222 — — 3333 !!!! 4444 &&&& 5555 %%%% 6666 ???? 7777"


# b = ''
#
# old_value = input("enter old value:")
#
# new_value = input("enter new value:")
#
# for i in a:
#     if (i == old_value):
#         b = b + new_value
#     else:
#         b = b + i

# student = "mathan"

#
# num="asdasfsegew5as324tsdaaw"
#
# split_range = 2
# split_text = ''
#
#
# i = 0
# for itr in num:
#     split_text = split_text + itr
#     i += 1
#     if i == split_range:
#         print(split_text)
#         i = 0
#         split_text = ''

#
# split_range = 2
# for itr in range(0,len(num),split_range):
#     if (len(num[itr:itr+split_range]) == split_range):
#         print(num[itr:itr+split_range])



# ind = 0
# sum = 0
#
# for i in range(len(num)):
#
#     if i%2 == 0 and ind == 0:
#         sum = sum + int(num[i])
#     elif i%2 !=0 and ind == 1:
#         sum = sum + int(num[i])
#
# print(sum)









# new_str = ''
#
# pos = 0
# for i in range(len(student)):
#     if (i % 2 == 0 and pos == 0):
#         new_str = new_str + '#'
#     elif(i % 2 != 0 and pos == 1):
#         new_str = new_str + '#'
#     else:
#         new_str = new_str + student[i]
#
# print(student)
# print(new_str)











# if pos == 0:
#     for i in range(len(student)):
#         if (i%2 == 0 and pos == 0):
#             new_str= new_str + '#'
#         else:
#             new_str = new_str + student[i]
# else:
#     for i in range(len(student)):
#         if (i%2 != 0):
#             new_str= new_str + '#'
#         else:
#             new_str = new_str + student[i]
#
# num = "1235162826346171623826"
#
# split_range = int(input("enter split range:"))
#
# for i in range(0,len(num),split_range):
#     if len(num[i:i+split_range]) == split_range :
#         print(num[i:i + split_range])

# str = "jkuiasnlzcpuasmnkuasanmajhguytuf"
# new_str = ''
# search = "a"
# for i in range(len(str)):
#     if(i%2 != 0):
#         new_str = new_str + str[i].upper()
#     else:
#         new_str = new_str + str[i]
#
#
# print(str)
# print(new_str)


# while True:
#     def func(a):
#         if a % 2 == 0:
#             print("Given number is even")
#         else:
#             print("given number is odd")
#
#
#     a = int(input("enter the a value:"))
#     func(a)

# a = input("enter string:")
#
# counter = 0
#
# while counter < (len(a)):
#     print(a[counter])
#
#     counter = counter + 1

a = 18
i = 1
count = 0
while i <= a:
    if (i % 2) == 1:
        count =count +1
    i = i + 1
print(count)