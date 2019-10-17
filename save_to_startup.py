import os
fp="" #filepath to start
uname=os.path.join(os.path.expandvars("%userprofile%"),"Documents and Settings").split("\\")
os.chdir("C:/Users/"+uname[2]+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
with open("start.bat","w") as god:
    god.write('start '+fp)
    god.close()
