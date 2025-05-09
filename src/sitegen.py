from os import path,listdir,mkdir
from os.path import splitext
from shutil import copy,rmtree
from convertors import markdown_to_html_node
import re

def copy_content(src_dir,dest_dir):
    if path.isdir(dest_dir):
        # print(f"Dest contents: {listdir(dest_dir)}")
        rmtree(dest_dir)
    mkdir(dest_dir)
    # print(f"Src contents: {listdir(src_dir)}")
    # current_src_dir = src_dir
    # current_dest_dir = dest_dir
    dir_content = []
    dir_content = listdir(src_dir)
    for obj in dir_content:
        if path.isfile(path.join(src_dir,obj)):
            copy(path.join(src_dir,obj),path.join(dest_dir,obj))
        if path.isdir(path.join(src_dir,obj)):
            # mkdir(path.join(dest_dir,obj))
            current_src_dir = path.join(src_dir,obj)
            current_dest_dir = path.join(dest_dir,obj)
            copy_content(current_src_dir,current_dest_dir)
                   
def extract_title(markdown):
    if re.search("(?:^# )(.*)",markdown) is None:
        raise Exception("No valid header found")
    return re.search("(?:^# )(.*)",markdown).group(1)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        src_md = f.read()
    
    with open(template_path, 'r') as f:
        html_template = f.read()
    
    # print(f"Src MD: {src_md}")
    # print(f"HTML Template: {html_template}")
    
    html_nodes = markdown_to_html_node(src_md)
    html = html_nodes.to_html()
    
    md_title = extract_title(src_md)
    
    final_html = html_template.replace("{{ Title }}",md_title).replace("{{ Content }}",html)
    
    with open(dest_path, 'w') as f:
        f.write(final_html)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content = []
    dir_content = listdir(dir_path_content)
    
    if not path.isdir(dest_dir_path):
        mkdir(dest_dir_path)
    
    for obj in dir_content:
        if path.isfile(path.join(dir_path_content,obj)):
            print(f"Split Ext:{splitext(obj)[0]}.html")
            generate_page(path.join(dir_path_content,obj),template_path,path.join(dest_dir_path,f"{splitext(obj)[0]}.html"))                
        if path.isdir(path.join(dir_path_content,obj)):
            # mkdir(path.join(dest_dir,obj))
            current_src_dir = path.join(dir_path_content,obj)
            current_dest_dir = path.join(dest_dir_path,obj)
            generate_pages_recursive(current_src_dir,template_path,current_dest_dir)