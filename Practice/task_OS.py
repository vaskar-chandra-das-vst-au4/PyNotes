# import os
# import shutil

# Note -Just put r before your normal string. It converts a normal string to a raw string:
# 1. pandas.read_csv(r"C:\Users\DeePak\Desktop\myac.csv")
# 2. pandas.read_csv("C:/Users/DeePak/Desktop/myac.csv") # not working
# 3. pandas.read_csv("C:\\Users\\DeePak\\Desktop\\myac.csv")
# path containing double backward slash is a raw string and python wants a raw string only

# print(os.getcwd())
# print(os.listdir())

# if os.path.exists(r"C:\Users\Vaskar\Desktop\Code_Files\Python\dataRenamed"):
#     # files = os.listdir(r"C:\Users\Vaskar\Desktop\Code_Files\Python\dataRenamed")
#     for x in range(51):
#         os.rename(
#             rf"C:\Users\Vaskar\Desktop\Code_Files\Python\dataRenamed\Day {x}",
#             rf"C:\Users\Vaskar\Desktop\Code_Files\Python\dataRenamed\Folder {x}",
#         )
# if os.path.exists("C:\\Users\\Vaskar\\Desktop\\Code_Files\\Python\\dataRenamed"):
#     # files = os.listdir(r"C:\Users\Vaskar\Desktop\Code_Files\Python\dataRenamed")
#     for x in range(51):
#         os.rename(
#             f"C:\\Users\\Vaskar\\Desktop\\Code_Files\\Python\\dataRenamed\\Day {x}",
#             f"C:\\Users\\Vaskar\\Desktop\\Code_Files\\Python\\dataRenamed\\Folder {x}",
#         )

# os.rmdir() # remove only empty dir , throw error if not found
# os.remove() # remove files only # throw error if not found
# os.rmdir("C:\\Users\\Vaskar\\Desktop\\Code_Files\\Python\\dataRenamed")
# print("rmdir" in dir(os))

# ! This removes the whole tree.
# shutil.rmtree("C:\\Users\\Vaskar\\Desktop\\Code_Files\\Python\\dataRenamed")
