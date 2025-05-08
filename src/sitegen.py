from os import path,listdir,mkdir
from shutil import copy,rmtree

def copy_content(src_dir,dest_dir):
    if path.isdir(dest_dir):
        print(f"Dest contents: {listdir(dest_dir)}")
        rmtree(dest_dir)
    mkdir(dest_dir)
    print(f"Src contents: {listdir(src_dir)}")
    # current_src_dir = src_dir
    # current_dest_dir = dest_dir
    dir_content = []
    dir_content = listdir(src_dir)
    for obj in dir_content:
        if path.isfile(path.join(src_dir,obj)):
            copy(path.join(src_dir,obj),path.join(dest_dir,obj))
        if path.isdir(path.join(src_dir,obj)):
            mkdir(path.join(dest_dir,obj))
            current_src_dir = path.join(src_dir,obj)
            current_dest_dir = path.join(dest_dir,obj)
    copy_content(current_src_dir,current_dest_dir)
            
            
    