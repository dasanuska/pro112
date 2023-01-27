import os
import shutil

#.exe, .msi, .gif, .png, .jpg, .jpeg, .csv, .pdf, .xsl, .xlsx, .ppt, .pptx

from_dir ="c:/users/ADMIN/Downloads"
to_dir ="c:/whitehatjr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

#Move ALL Image file from Downloads Folder To Another Folder
for file_name in list_of_files:

    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension =='':
        continue
    if extension in ['.txt','.pdf','.doc','.docx']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' +"Document_Files"
        path3 = to_dir + '/' +"Document_Files" + file_name
        #print("path1",path1)
        #print("path3",path3)




        if os.path.exists(path2):
            print("Moving" + file_name + ".....")

            #Move from path1 -----> path3
            shutil.move(path1,path3)

        else:
            os.markdirs(path2)
            print("Moving" + file_name + ".....")
            shutil.move(path1,path3)