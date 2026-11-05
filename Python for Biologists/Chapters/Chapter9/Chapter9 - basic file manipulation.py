import os
#os.rename(r'C:\Users\Admin\Desktop\for example\old.txt', r'C:\Users\Admin\Desktop\for example\new.txt')

#above is when the file is not in the folder we are working in but somewhere in the system so we use the path
#if file is in folder

#os.rename('banku.txt', 'kenkey.txt')

#The reason i am commenting the code after i run them is that the code was to change banku to kenkey after running we have kenkey on ,so if i write a new code trying to work on another file the os.rename('banku.txt', 'kenkey.txt')will also run ,but now the is no banku file only kenkey so we will get an error

#If we specify a different folder, but the same file name, in the second argument, then the function will move the file from one folder to another:

#os.rename (r'C:\Users\Admin\Desktop\for example\new.txt' , r'C:\Users\Admin\Desktop\Bioinformatics\Python for Biologists\Chapters\Chapter9\new.txt')

#Of course, we can move and rename a file in one step too

#os.rename (r'C:\Users\Admin\Desktop\Bioinformatics\Python for Biologists\Chapters\Chapter9\new.txt' , r'C:\Users\Admin\Desktop\for example\old.txt')

#you can also change the name of folders too

#os.rename (r'C:\Users\Admin\Desktop\for example' , r'C:\Users\Admin\Desktop\FOR EXAMPLE')

#If we try to move a file to a folder that doesn't exist we'll get an error. We need tocreate the new folder first with the os.mkdir function

#os.mkdir (r'C:\Users\Admin\Desktop\Bioinformatics\Python for Biologists\Chapters\Chapter9\my examples')

#If we need to create a bunch of directories all in one go, we can use the os.makedirs function
#it create each individual path,instead of mkdir which only creates the last path

#os.makedirs (r'C:\Users\Admin\Desktop\makedirs\folder1\folder2\folder3\folder4\bye bye\last.txt', exist_ok=True)
#it creates every single folder on the way to last.txt - the only thing is that last.txt is made as a folder and not a file
#Adding exist_ok=True prevents Python from throwing a FileExistsError if the target folder already exists.so with the code i can leave it uncommented

#To copy a file or folder we use the shutil module. We can copy a single file with 
#shutil.copy for file
#shutil.copytree for folder
import shutil

#shutil.copy ('kenkey.txt' ,'kenkey3.txt')
#shutil.copytree ('my examples' , r'my example(copy2)')

#Deleting files and folders
#To delete a single file, use os.remove
#os.remove ('kenkey2.txt')

#To remove an empty folder use os.rmdir
#os.rmdir (r'my example(copy1)')

#To delete a folder and all the files in it, use shutil.rmtree
#shutil.rmtree (r'C:\Users\Admin\Desktop\makedirs')

#Listing folder contents
#os.listdir

for file in os.listdir(r"C:\Users\Admin\Desktop\Art books"):
    print('the file is ' + file)

print('\n')
#To get a list of the contents of the current working directory, use the string "." for the path:
for file in os.listdir('.'):
    print('file name is ' + file)