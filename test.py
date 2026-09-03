# f=open("hello.txt")
# print(f.read())

# f=open("bye.txt","x")


with open("bye.txt","a") as f:
    f.write("testinggg")
with open("bye.txt","r") as r:
    print(r.read())

import os
os.remove("bye.txt")

