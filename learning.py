# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# mode = w : rewrite
# mode = a : append to exisitng text

# with open("my_file.txt", mode="w") as file:
#     contents = file.write("New text")
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nNew text 2")
#     print(contents)
#
# with open("new_file.txt", mode="w") as file:
#     contents = file.write("A new file as been created as it previously did not exist and I am using mode='w'")
#     print(contents)

with open(r"C:\Users\Antony\Desktop\new_file.txt", mode="a") as file:
    contents = file.write("\nCan't get away from me")

with open("/Users/Antony/Desktop/new_file.txt", mode="a") as file:
    contents = file.write("\nCan't get away from me 2")

with open("../../../../Desktop/new_file.txt", mode="a") as file:
    contents = file.write("\nCan't get away from me 3")
