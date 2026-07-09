import os

print(os.path.exists("my folder"))

print(os.path.isfile("hello.txt"))
print(os.path.isdir("documents"))

print(os.path.getsize("hello.txt"))

path = os.path.join("data", "logs", "app.log")
print(path)
