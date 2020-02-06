from pathlib import Path

#absolute path
#c:\program files\microsoft

#relative path

path=Path("ecommerce")
print(path.exists())


#to make a new directory
path=Path("emails")
print(path.mkdir())       #replace mkdir with rmdir to remove directory

path=Path()
print(path.glob("*.*")) # to search for everything
print(path.glob("*.py"))  #to search for all python files
print(path.glob("*.xls")) #to search for all the excel files 


#to iterate over and see all files 
path=Path()
for file in path.glob("*.py"):
    print (file)