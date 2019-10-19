import winreg as reg
import os
def wtr():
    pth=os.path.dirname(os.path.realpath(__file__))
    s_name="main.py"
    address=os.path.join(pth,s_name)
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
    reg.CloseKey(open) 
if __name__=="__main__":
    wtr()
