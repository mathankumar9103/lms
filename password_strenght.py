password = "asdkaaaaaa@"

no = ''
l_char = ''
u_char = ''
spc_char = ''

for i in password:

    if (ord(i) >= 48) and (ord(i) <= 57):
        if i not in no:
            no = no +i

    elif (ord(i) >= 97) and (ord(i) <= 122):
        if i not in l_char:
            l_char = l_char + i

    elif (ord(i) >= 65) and (ord(i) <= 90):
        if i not in u_char:
            u_char = u_char + i

    else:
        if i not in spc_char:
            spc_char = spc_char + i

# print(no)
# print(l_char)
# print(u_char)
# print(spc_char)

pass_strength = (len(no) * 2) + (len(l_char) * 4) + (len(u_char) * 4) + (len(spc_char) * 6)

print("password strength:",int(pass_strength))

if (len(password) >= 8) and (len(no) >= 1) and (len(l_char) >= 1) and (len(u_char) >= 1) and (len(spc_char) >= 1) and (pass_strength >= 30):
    print("Valid password")

else:
    print("invalid password")
    if (len(password) < 8):
        print("password length must be greater than 8")
    if (len(no) < 1):
        print("password should have atleast one number")
    if (len(l_char) < 1):
        print("password should have atleast one lowercase")
    if (len(u_char) < 1):
        print("password should have atleast one uppercase")
    if (len(spc_char) < 1):
        print("password should have atleast one special character")
    if (pass_strength < 30):
        print("password strength should be greater than 30")