import subprocess

with open("E:\\Code_Files\\Python\\CreatedFiles\\output.txt", "wb") as output:
    subprocess.check_call(["python", "fileHandling.py"], stdout=output)
    print("Output written successfully!")

# "E:\\Code_Files\\Python\\CreatedFiles\\output.txt" - Location of your file where you want to copy the output.
# wb - write and open in binary.
# output - file object(file where output data of "fileHandling.py" will be stored.)
# ["python", "fileHandling.py"] 0 - is fixed 1- name of the file whose output you are going to write.
# stdout=output - output file object name
