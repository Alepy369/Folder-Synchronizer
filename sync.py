from pathlib import Path
import os 
import path
import shutil
import sys
import logging

def create_log():
    logging.basicConfig(filename='logs.txt', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logging.info('is when this event was logged.')
create_log()

#is_file=os.path.isfile(source_path)
#print(is_file)
#is_dir=os.path.isdir(source_path) 
#print(is_dir)

# Instantiate the Path class
#obj = Path(source_path + '/this_is_the_source_folder.txt')
# Check if path exists
#print("path exists?", obj.exists())

list_file_paths_source=[]
list_dir_paths_source=[]
list_dir_paths_replica=[]
list_file_paths_replica=[]

def list_files_and_folders(dir):
    if dir == source_path:
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)
            if os.path.isfile(item_path):
                #print(f"    File: {item}")
                list_file_paths_source.append(item_path)
            elif os.path.isdir(item_path):
                #print(f"    Folder: {item}")
                list_files_and_folders(item_path)  # Recursively call the function for subdirectories
                list_dir_paths_source.append(item_path)

    if dir == replica_path:
        for item in os.listdir(replica_path):
            item_path = os.path.join(replica_path, item)
            if os.path.isfile(item_path):
                #print(f"    File: {item}")
                list_file_paths_replica.append(item_path)
            elif os.path.isdir(item_path):
                #print(f"    Folder: {item}") 
                list_files_and_folders(item_path) # Recursively call the function for subdirectories 
                list_dir_paths_replica.append(item_path)

items_not_in_replica=[]

def check_files_and_folders(list_file_paths_source, list_file_paths_replica, list_dir_paths_source, list_dir_paths_replica):
    for fpath in list_file_paths_source:
        name_item=str(fpath).removeprefix('/').split('/')[-1]
        try:
            if fpath not in list_file_paths_replica:
                print(f'The file "{name_item}" is not on replica folder')
                items_not_in_replica.append(fpath)
        
        except FileNotFoundError as e:
            print(e)

    for dpath in list_dir_paths_source:
        name_item=str(dpath).removeprefix('/').split('/')[-1]
        try:
            if fpath not in list_dir_paths_replica:
                print(f'The file "{name_item}" is not on replica folder')
                items_not_in_replica.append(fpath)
        
        except FileNotFoundError as e:
            print(e)

        # if name_item not in os.listdir(dpath):
        #     print(name_item)
        #     #items_not_in_replica.append(dpath)
        #     #print(f'The dir "{name_item}" is not on replica folder')
        # else:
        #     pass
        

source_path = '/home/alepy/Folder-Synchronizer/source'
replica_path = '/home/alepy/Folder-Synchronizer/replica'

#print('Source Folder Content:')
list_files_and_folders(source_path)
#print(list_dir_paths_source)
#print()
#print('Replica Folder Content:')
#list_files_and_folders(replica_path)


#print('Files not in replica folder:')
#check_files_and_folders(list_file_paths_source, list_file_paths_replica, list_dir_paths_source, list_dir_paths_replica)

#print(items_not_in_replica)

# path_w='/home/alepy/Folder-Synchronizer/source/world/Portugal'

# if path_w in list_dir_paths_replica:
#     print("dir is in replica folder")
# else:
#     print('nope')

def list_files_and_folders_source(directory):
    for item in os.listdir(directory):
        #print(item)
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print(f"File: {item}")
        elif os.path.isdir(item_path):
            print(f"Folder: {item}")
            list_files_and_folders(item_path)  # Recursively call the function for subdirectories

list_files_and_folders_source(source_path)