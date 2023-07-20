import os
import shutil

fromdir = "D:\Books"
todir = "D:\Document_Files"
list_of_files = os.listdir(fromdir)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == '':
        continue


if extension in ['.pdf', '.doc', '.png', '.jpg', '.htm']:
    path1 = fromdir + '/' + file_name
    path2 = todir + '/' + "Document_Files"
    path3 = todir + '/' + "Document_Files" + '/' + file_name
    print("path1", path1)
    print("path3", path3)

if os.path.exists(path2):
    print("Moving"+ file_name + "......")

    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Moving" + file_name + ".......")
    shutil.move(path1, path3)
