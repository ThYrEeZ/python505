import os

def list_dir(path):
    for item in os.listdir(path):
        full_path = os.path.join(path,item)
        print(full_path)

        if os.path.isdir(full_path):
            list_dir(full_path)

list_dir("C:\Program Files (x86)")