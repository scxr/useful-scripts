import os
fp="" #filepath to start
os.chdir("C:/Users/"+os.path.expandvars("%userprofile%").split("\\")[2]+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
with open("start.bat","w") as god:
    god.write('start '+fp)
    god.close()
