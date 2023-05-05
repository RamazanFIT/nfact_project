str1 = input()
str2 = input()

if len(str1) != len(str2):
    print('no')
    exit()
elif sorted(str1) == sorted(str2):
    print("yes")
else:
    print("no")