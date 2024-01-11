import os 
import sys
import logging


source_path = '/home/alepy/Folder-Synchronizer/source'
replica_path = '/home/alepy/Folder-Synchronizer/replica'


list_file_paths_source=[]
list_dir_paths_source=[]
list_dir_paths_replica=[]
list_file_paths_replica=[]

list_file_source=[]
list_dir_source=[]
list_dir_replica=[]
list_file_replica=[]


def get_source_content(directory):

    for item in os.listdir(directory):
        #print(item)
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            #print(f"File: {item}")
            list_file_paths_source.append(item_path)
            list_file_source.append(item)
        elif os.path.isdir(item_path):
            #print(f"Folder: {item}")
            list_dir_paths_source.append(item_path)
            list_dir_source.append(item)
            get_source_content(item_path)  # Recursively call the function for subdirectories
    
    return list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source


def get_replica_content(directory):

    for item in os.listdir(directory):
        #print(item)
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            #print(f"File: {item}")
            list_file_paths_replica.append(item_path)
            list_file_replica.append(item)
        elif os.path.isdir(item_path):
            #print(f"Folder: {item}")
            list_dir_paths_replica.append(item_path)
            list_dir_replica.append(item)
            get_source_content(item_path)  # Recursively call the function for subdirectories
            
    return list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica

#get_source_content(source_path)
#get_replica_content(replica_path)

items_not_in_replica = {"Files": [], "Dirs": []}

def check_files_and_folders(list_file_source, list_file_replica, list_dir_source, list_dir_replica):

    for file_name in list_file_source:
        try:
            if file_name not in list_file_replica:
                print(f'The file "{file_name}" is not on replica folder')
                items_not_in_replica['Files'].append(file_name)
            else:
                pass
        
        except FileNotFoundError as e:
            print(e)
    

    for dir_name in list_dir_source:
        try:
            if dir_name not in list_dir_replica:
                print(f'The folder "{dir_name}" is not on replica folder')
                items_not_in_replica['Dirs'].append(dir_name)
            else:
                pass
        
        except FileNotFoundError as e:
            print(e)
                    
    return items_not_in_replica


def create_dicts():
    
    dict_paths={}
    dict_files_and_folders={}

    dict_paths["Files_from_sorce"]=list_file_paths_source
    dict_paths["Folders_from_sorce"]=list_dir_paths_source
    dict_paths["Files_from_replica"]=list_file_paths_replica
    dict_paths["Files_from_replica"]=list_dir_paths_replica

    dict_files_and_folders["Files_from_sorce"]=list_file_source
    dict_files_and_folders["Folders_from_sorce"]=list_dir_source
    dict_files_and_folders["Files_from_replica"]=list_file_replica
    dict_files_and_folders["Files_from_replica"]=list_dir_replica

#create_dicts()

def log_create():
    logging.basicConfig(filename='logs.txt', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logger = logging.getLogger('createFileOrFolder')
    logger.info('Created a file or folder')

def log_copy():
    logging.basicConfig(filename='logs.txt', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logger = logging.getLogger('copyFileOrFolder')
    logger.info('Copied a file or folder')

def log_remove():
    logging.basicConfig(filename='logs.txt', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logger = logging.getLogger('removeFileOrFolder')
    logger.info('Removed a file or folder')