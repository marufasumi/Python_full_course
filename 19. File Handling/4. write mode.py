# with open("new.txt", "w") as f:
#     f.write("Hello World\n")
#     f.write("Good bye\n")

lines = ["first line\n", "abcd\n", "dhajkdhwajkdhwak\n"]
with open("new.txt", "w") as f:
    f.writelines(lines)
