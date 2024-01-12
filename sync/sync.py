import os 
import logging
import path

list_file_paths_source=[]
list_dir_paths_source=[]
list_dir_paths_replica=[]
list_file_paths_replica=[]

list_file_source=[]
list_dir_source=[]
list_dir_replica=[]
list_file_replica=[]


source_path = '/home/alepy/Folder-Synchronizer/source'
replica_path = '/home/alepy/Folder-Synchronizer/replica'
log_file_path= '/home/alepy/Folder-Synchronizer/logs.txt'

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

get_source_content(source_path)
get_replica_content(replica_path)

items_not_in_replica = {"Files": [], "Dirs": []}

def check_files_and_folders():

    for file_path in list_file_paths_source:
        replica_path=file_path.replace("/source","/replica")
        #print(replica_path)
        #print(file_path)
        try:
            if replica_path not in list_file_paths_replica:
                file_name=file_path.split('/')[-1]
                #print(f'The file "{file_name}" is not on replica folder')
                items_not_in_replica['Files'].append(file_path)
            else:
                pass
        
        except FileNotFoundError as e:
            print(e)
    

    for dir_path in list_dir_paths_source:
        replica_path=dir_path.replace("/source","/replica")
        try:
            if replica_path not in list_dir_paths_replica:
                dir_name=dir_path.split('/')[-1]
                #print(f'The folder "{dir_name}" is not on replica folder')
                items_not_in_replica['Dirs'].append(dir_path)
            else:
                pass
        
        except FileNotFoundError as e:
            print(e)
                    
    return items_not_in_replica

def log_create(log_path, log_text):
    logging.basicConfig(filename=log_path, encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logger = logging.getLogger('createFileOrFolder')
    logger.info(log_text)

def log_copy(log_path, log_text):
    logging.basicConfig(filename=log_path, encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logger = logging.getLogger('copyFileOrFolder')
    logger.info(log_text)
    
def log_remove(log_path, log_text):
    logging.basicConfig(filename=log_path, encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S %a', level=logging.INFO) 
    logger = logging.getLogger('removeFileOrFolder')
    logger.info(log_text)

def create_file(path, log_path):
    name=path.split('/')[-1]
    folder_path=os.path.dirname(path)
    if os.path.exists(path) == False:
        os.system("touch " + path)
        log_text=f'-- CREATING FILE -- "{name}" in "{folder_path}"'
        log_create(log_path, log_text)
    else:
        print(f'File "{name}" already exists')

def create_dir(path, log_path):
    name=path.split('/')[-1]
    folder_path=os.path.dirname(path)
    if os.path.exists(path) == False:
        os.system("mkdir " + path)
        log_text=f'-- CREATING FOLDER -- "{name}" in "{folder_path}"'
        log_create(log_path, log_text)
    else:
        print(f'Folder "{name}" already exists')

def copy(path1, path2, log_path):
    name=path1.split('/')[-1]
    folder_path1=os.path.dirname(path1)
    if os.path.exists(path1):
        if os.path.isfile(path1):
            os.system("cp " + path1 + " " + path2)
            log_text=f'-- COPYING FILE -- "{name}" from "{folder_path1}" to "{path2}"'
            log_copy(log_path, log_text)
        elif os.path.isdir(path1):
            os.system("cp -r " + path1 + " " + path2)
            log_text=f'-- COPYING FOLDER -- "{name}" from "{folder_path1}" to "{path2}"'
            log_copy(log_path, log_text)
    else:
        print(f'File or folder "{name}" does not exist')

def remove(path, log_path):
    name=path.split('/')[-1]
    folder_path=os.path.dirname(path)
    if os.path.exists(path):
        if os.path.isfile(path):
            os.system("rm " + path)
            log_text=f'-- REMOVING FILE -- "{name}" from "{folder_path}"'
            log_remove(log_path, log_text)
        elif os.path.isdir(path):
            if not os.listdir(path):
                print('Deleting empty folder... proceeding')
                os.system("rm -d " + path)
                log_text=f'-- REMOVING EMPTY FOLDER -- "{name}" from "{folder_path}"'
                log_remove(log_path, log_text)
            else:
                print('ALERT!')
                y=input(f'The folder "{name}" is not empty, do you want to delete it and all its content? (y/n) ')    
                if y.lower()=='y':
                    print('Deleting folder and all its content')
                    os.system("rm -r " + path)
                    log_text=f'-- REMOVING NON EMPTY FOLDER -- "{name}" from "{folder_path}"'
                    log_remove(log_path, log_text)
                elif y.lower()=='n':
                    pass

    else:
        print(f'File or folder "{name}" does not exist')

#create_dir('/home/alepy/Folder-Synchronizer/abc', log_path)
#create_file('/home/alepy/Folder-Synchronizer/def.txt', log_path)
#create_file('/home/alepy/Folder-Synchronizer/abc/def.txt', log_path)
    
#copy('/home/alepy/Folder-Synchronizer/abc', '/home/alepy/Folder-Synchronizer/z', log_path)
#copy('/home/alepy/Folder-Synchronizer/abc/def.txt', '/home/alepy/Folder-Synchronizer/z/abc.txt', log_path)
        
#remove('/home/alepy/Folder-Synchronizer/def.txt', log_path)
#remove('/home/alepy/Folder-Synchronizer/abc', log_path)
#remove('/home/alepy/Folder-Synchronizer/z/def.txt', log_path)
#remove('/home/alepy/Folder-Synchronizer/z/abc.txt', log_path)
#remove('/home/alepy/Folder-Synchronizer/z', log_path)

check_files_and_folders()

def to_sync():

    for category, items in items_not_in_replica.items():
        for dir_path in items:
            if os.path.isdir(dir_path):
                folder_name=dir_path.split('/')[-1]
                replica_path=dir_path.replace("/source","/replica")
                create_dir(replica_path, log_file_path)

    for category, items in items_not_in_replica.items():
        for file_path in items:
            if os.path.isfile(file_path):
                file_name=file_path.split('/')[-1]
                replica_path=file_path.replace("/source","/replica")
                create_file(replica_path, log_file_path)
    
    for file_path_replica in list_file_paths_replica:
        source_path=file_path_replica.replace("/replica","/source")
        if source_path in list_file_paths_source:
            copy(source_path, file_path_replica, log_file_path)

    for file_path_replica in list_file_paths_replica:
        source_path=file_path_replica.replace("/replica","/source")
        if source_path not in list_file_paths_source:
            remove(file_path_replica, log_file_path)
    
    for dir_path_replica in list_dir_paths_replica:
        source_path=dir_path_replica.replace("/replica","/source")
        if source_path not in list_dir_paths_source:
            print(f'hey {dir_path_replica} is in replica but not on source')
            print()
            remove(dir_path_replica, log_file_path)
            
to_sync()

'''
se tiver na source e não na replica -> items_not_in_replica

oq tá na source -> list_file_source, list_dir_source

oq tá na replica -> list_file_replica, list_dir_replica
'''

#create_file('/home/alepy/Folder-Synchronizer/source/this_is_the_source.txt', log_file_path)
#create_file('/home/alepy/Folder-Synchronizer/replica/this_is_the_source.txt', log_file_path)