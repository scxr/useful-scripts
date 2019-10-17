import psutil,os
for proc in psutil.process_iter():
    try:
        p=psutil.Process(os.getpid())
        for dll in p.memory_maps():
            print(os.getpid(),dll.path)
            
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
