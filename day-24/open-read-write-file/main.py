# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# by using 'with open() as X', you don't have to close the file.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# how to write in your file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# if you don't want to remove previous texts
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# if your opening a file that doesn't exists, it will create one (but only in w mode).
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
