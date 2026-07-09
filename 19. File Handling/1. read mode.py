# f = open("hello.txt", "r")
# content = f.read(10)
# print(content)
# content1 = f.read(10)
# print(content1)
# f.close()

with open("hello.txt", "r") as f:
    content = f.read(10)
    print(content)
    content1 = f.read(10)
    print(content1)

# C:\Users\Code and Debug\Desktop\Python_Codes\19. File Handling

"""
script

open("C:\Users\Code and Debug\Desktop\Python_Codes\19. File Handling\new.txt")
"""
