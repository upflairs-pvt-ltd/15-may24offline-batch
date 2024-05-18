# module , 
import os ## 

# pwd 
# print("my current working dir : ",os.getcwd())

# os.chdir("E:\HD images")
# print("after chdir : ",os.getcwd())
# lst =  os.listdir()
# print("no of images : ",len(lst))

# os.mkdir('testing2')
# os.makedirs('testing2',exist_ok=True)
# os.rmdir() ,os.removedirs()

# print('folder is created')
path1 = r"C:\Users\Ranjit"
path2 = r"Desktop\jodhpur"
# complete_path = r"C:\Users\Ranjit\Desktop\jodhpur"
complete_path = os.path.join(path1,path2)
print("jodhpur folder complete path : ",complete_path)

os.chdir(complete_path)
print("now i m in jodhpur")

if os.path.exists('hello.txt'):
    print("your file is present")
else:
    text_file = open("hello.txt",'x')
    print("your file is opened and created")

# file handling , exception handling




# path = relative , absolute , python path 
# absolute path --> E:\HD images,proper address
# relative path --> testing


# offline batch --> day4.py