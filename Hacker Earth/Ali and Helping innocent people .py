# def checkNumber(num):
#     check = ["A", "E", "I", "O", "U", "Y"]
#
#     digit = ""
#     for i in num:
#         if i.upper() in check:
#             return "invalid"
#         else:
#             pass
#         if i.isdigit():
#             digit += i
#         if len(digit) == 2:
#             add = 0
#             convert = int(digit)
#             while convert > 0:
#                 add += (convert % 10)
#                 convert = convert // 10
#
#             if add % 2 == 0:
#                 digit = ""
#                 pass
#             else:
#                 return "invalid"
#     return "valid"
#
# n = input()
# print(checkNumber(n))

s = input()

v = s[2]

l = ["A","E","I","O","U","Y"]

if v in l:
    print("invalid")

else:
    if (((int(s[0])+int(s[1]))) % 2 == 0) and (((int(s[3])+int(s[4]))) % 2 == 0) and (((int(s[4])+int(s[5]))) % 2 == 0) and (((int(s[7])+int(s[8]))) % 2 == 0):
        print('valid')
    else:
        print('invalid')