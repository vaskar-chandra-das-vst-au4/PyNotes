# newFile = open("E:\\Code_Files\\Python\\CreatedFiles\\A.txt", "r+")
# newFile.write(
#     "Python Tutorial \n**This file is created using Python**\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Qui dicta minus molestiae vel beatae natus eveniet ratione temporibus aperiam harum alias officiis assumenda officia quibusdam deleniti eos cupiditate dolore doloribus."
# )
# print("Data written successfully!")

# print(newFile.read())
# newFile.close()
# print("File Closed")

# # WRITE TO A FILE
# try:
#     fileA = open("E:\\Code_Files\\Python\\CreatedFiles\\A.txt", "a")
#     # fileA.write("THIS LINE IS APPENDED LATER!!!")
#     print(fileA.read())
# finally:
#     fileA.close()
# print("File Closed!")

# # READ FILE CONTENT
# with open("E:\\Code_Files\\Python\\CreatedFiles\\A.txt") as fileA:
#     print(fileA.read())
#     # OR
# with open("E:\\Code_Files\\Python\\CreatedFiles\\A.txt") as fileA:
#     for x in fileA:
#         print(x)

# FILE POINTER
# fileObj.tell() - return the byte number where the file pointer currently exists
with open("E:\\Code_Files\\Python\\CreatedFiles\\A.txt") as fileA:
    print(fileA.tell())
    fileA.read()
    print(fileA.tell())
