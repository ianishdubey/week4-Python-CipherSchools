# read file
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

# print(f'cursor position- {f.tell()}')

# print(f.read())
# print(f.readline(), end='')
# print(f.readline)
# print(f.readline)
# print(f'cursor position- {f.tell()}')   # OR f.tell()
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f'cursor position- {f.tell()}')   # OR f.tell()
# print(f.read())

# lines = f.readlines()
# print(len(line())
# for line in lines
#     print(line,end='')

f = open("D:\week4 Python\file1.txt")

# \n, \t
# windows - \
# linux,mac - /

# name , closed
for line in f.readlines():
    print(line,end='')

f.close()