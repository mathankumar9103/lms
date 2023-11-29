# chunk
# def m_chunk(inp,size):
#     out = []
#
#     for itr in range(0,len(inp),size):
#        out.append(inp[itr:itr+size])
#     return out
#
#
# print(m_chunk([1,2,3,4], 2))

# compact
#
# def m_compact(inp):
#     out = []
#     for i in inp:
#         if i != "False" and i != "null" and i != 0 and i != "" and i != "undefined" and i != "NaN":
#             out.append(i)
#     return out
# print(m_compact([1,0,False,2,'undefined',3,"",4,"null",5,"NaN"]))

#concat
#
# def m_concat(array,values):
#     out = []
#     out = array + values
#     return out
# print(m_concat([1],2,3,[4]))

#difference
#
# def difference(array,value):
#     out = []
#     for i in array:
#         if i not in value:
#             out.append(i)
#     return out
# print(difference([1,2,3,4,5],[4,5]))

#drop

# def drop(arr, ind):
#     a1 = []
#     for i in range(ind):
#         a1.append(arr[i])
#         arr.pop(i)
#     return a1
#
# array = [1,2,3,4,5,6]
# print(drop(array,3))
# print(array)




























#String_replace

# string = "python programmer"
# present_value = input("Enter the value:")
# replaced_value = input("enter value to change:")
# res = ""
# for i in string:
#     if present_value in string:
#         if i == present_value:
#             res += replaced_value
#         else:
#             res += i
#     else:
#         print("invalid one")
# print(res)

#shuffled_string

# string = input("Enter the string:")
# shuff = ""
# for i in range(0,len(string)):
#     idx = int(input("enter index:"))
#     shuff += string[idx]
# print(shuff)

#factors of a number

# n = int(input("enter:"))
# for i in range(1,n+1):
#     if (n%i) == 0:
#         print(i)

#prime_number

# n = int(input("enter the number:"))
# factors = 0
# for i in range(2,n):
#     if (n%i == 0):
#         factors += 1
# if factors == 0:
#     print("prime number")
# else:
#     print("Not a prime number")

#prime number in a range of values

#factorial of a number
#
# n = int(input("enter the number:"))
# if n < 0:
#     print("no factorial for negative numbers")
# elif n == 1:
#     print("1")
# else:
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

value = ord("9")
print(value)