import os,sys
import time
fts=os.getcwd()+"\main.py" #your file to start
user=os.getcwd().split('\\')
os.chdir("C:/Users/"+user[2]+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
with open("tst.bat","w") as f:
    f.write("start " + fts)
    f.close()
