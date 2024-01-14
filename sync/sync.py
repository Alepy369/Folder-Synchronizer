import os 
import logging
import hashlib

list_file_paths_source=[]
list_dir_paths_source=[]
list_dir_paths_replica=[]
list_file_paths_replica=[]

list_file_source=[]
list_dir_source=[]
list_dir_replica=[]
list_file_replica=[]

list_file_hash_source=[]
list_file_hash_replica=[]

def generate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()

def get_source_content(source_path, list_file_paths_source=None, list_dir_paths_source=None,
                        list_file_source=None, list_dir_source=None):
    
    # Initialize lists if not provided
    if list_file_paths_source is None:
        list_file_paths_source = []
    if list_dir_paths_source is None:
        list_dir_paths_source = []
    if list_file_source is None:
        list_file_source = []
    if list_dir_source is None:
        list_dir_source = []

    for item_s in os.listdir(source_path):
        item_path_s = os.path.join(source_path, item_s)

        if "/source" in item_path_s:
            if os.path.isfile(item_path_s):
                list_file_paths_source.append(item_path_s)
                list_file_source.append(item_s)

                hash=generate_sha256(item_path_s)
                list_file_hash_source.append(hash)
            elif os.path.isdir(item_path_s):
                list_dir_paths_source.append(item_path_s)
                list_dir_source.append(item_s)
                get_source_content(item_path_s, list_file_paths_source,
                                   list_dir_paths_source, list_file_source, list_dir_source)

    return source_path, list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source, list_file_hash_source

def get_replica_content(replica_path, list_dir_paths_replica=None, list_file_paths_replica=None, 
                        list_dir_replica=None, list_file_replica=None):
    
    # Initialize lists if not provided
    if list_dir_paths_replica is None:
        list_dir_paths_replica = []
    if list_file_paths_replica is None:
        list_file_paths_replica = []
    if list_dir_replica is None:
        list_dir_replica = []
    if list_file_replica is None:
        list_file_replica = []

    for item in os.listdir(replica_path):
        item_path = os.path.join(replica_path, item)

        if "/replica" in item_path:
            if os.path.isfile(item_path):
                list_file_paths_replica.append(item_path)
                list_file_replica.append(item)

                hash=generate_sha256(item_path)
                list_file_hash_replica.append(hash)
            elif os.path.isdir(item_path):
                list_dir_paths_replica.append(item_path)
                list_dir_replica.append(item)
                get_replica_content(item_path, list_dir_paths_replica, 
                                    list_file_paths_replica, list_dir_replica, list_file_replica)

    return replica_path, list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica, list_file_hash_replica

def check_files_and_folders(source_path, replica_path, list_file_paths_source, list_dir_paths_source,
                             list_file_paths_replica, list_dir_paths_replica):
    
    items_not_in_replica = {"Files": [], "Hashs": [], "Dirs": []}

    print("Checking files:")
    for file_path in list_file_paths_source:
        try:
            rep_path = os.path.join(replica_path, os.path.relpath(file_path, source_path))
            if not os.path.exists(rep_path):
                hash=generate_sha256(file_path)
                file_name = os.path.basename(file_path)
                print(f'    File: "{file_name}"')
                print(f'    Hash: "{hash}"')
                items_not_in_replica['Files'].append(file_path)
                items_not_in_replica['Hashs'].append(hash)

            else:
                file_name = os.path.basename(file_path)
                s_hash=generate_sha256(file_path)
                r_hash=generate_sha256(rep_path)

                if s_hash != r_hash:
                    print(f'    File {file_name} modified!')

        except FileNotFoundError as e:
            print(e)

    print("Checking folders:")
    for dir_path in list_dir_paths_source:
        try:
            rep_path = os.path.join(replica_path, os.path.relpath(dir_path, source_path))
            if not os.path.exists(rep_path):
                dir_name = os.path.basename(dir_path)
                print(f'    Folder: "{dir_name}"')
                items_not_in_replica['Dirs'].append(dir_path)

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
        print(f'File "{name}" already exists!')

def create_dir(path, log_path):
    name=path.split('/')[-1]
    folder_path=os.path.dirname(path)
    if os.path.exists(path) == False:
        os.system("mkdir " + path)
        log_text=f'-- CREATING FOLDER -- "{name}" in "{folder_path}"'
        log_create(log_path, log_text)
    else:
        print(f'Folder "{name}" already exists!')

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
        print(f'File or folder "{name}" does not exist!')
        
def remove(path, log_path):
    name = os.path.basename(path)
    folder_path = os.path.dirname(path)

    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            log_text = f'-- REMOVING FILE -- "{name}" from "{folder_path}"'
            log_remove(log_path, log_text)
        elif os.path.isdir(path):
            if not any(os.scandir(path)):
                os.system("rm -d " + path)
                log_text = f'-- REMOVING FOLDER -- "{name}" from "{folder_path}"'
                log_remove(log_path, log_text)
    else:
        print(f'File or folder "{name}" does not exist!')

def to_sync(result, list_file_paths_replica, list_dir_paths_replica, list_file_paths_source,
                 list_dir_paths_source, source_path, replica_path, log_file_path):

    print("Syncing...")

    for category, items in result.items():
        for dir_path in items:
            if os.path.isdir(dir_path):
                dir_name=dir_path.split('/')[-1]
                replica_path=dir_path.replace("/source","/replica")
                create_dir(replica_path, log_file_path)
                print(f'    Folder {dir_name} created!')

    for category, items in result.items():
        for file_path in items:
            if os.path.isfile(file_path):
                file_name=file_path.split('/')[-1]
                replica_path=file_path.replace("/source","/replica")
                create_file(replica_path, log_file_path)
                print(f'    File {file_name} created!')
                
    for file_path_replica in list_file_paths_replica:
        file_path_source = file_path_replica.replace("/replica", "/source")
        if file_path_source in list_file_paths_source:
            file_name = file_path_source.split('/')[-1]
            
            source_hash = generate_sha256(file_path_source)
            replica_hash = generate_sha256(file_path_replica)

            if source_hash != replica_hash:
                copy(file_path_source, file_path_replica, log_file_path)
                print(f'    File {file_name} copied!')

    for file_path_replica in list_file_paths_replica:
        file_path_source=file_path_replica.replace("/replica","/source")
        if file_path_source not in list_file_paths_source:
            file_name=file_path_source.split('/')[-1]
            remove(file_path_replica, log_file_path)
            print(f'    File {file_name} removed!')
    
    for dir_path_replica in list_dir_paths_replica:
        dir_path_source=dir_path_replica.replace("/replica","/source")
        if dir_path_source not in list_dir_paths_source:
            dir_name=dir_path_source.split('/')[-1]
            remove(dir_path_replica, log_file_path)
            print(f'    Folder {dir_name} removed!')

# s_path, list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source, list_file_hash_source=get_source_content('/home/alepy/Folder-Synchronizer/source')
# r_path, list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica, list_file_hash_replica=get_replica_content('/home/alepy/Folder-Synchronizer/replica')

# result = check_files_and_folders(s_path, r_path, list_file_paths_source, 
#                                  list_dir_paths_source, list_file_paths_replica, list_dir_paths_replica)

# to_sync(result, '/home/alepy/Folder-Synchronizer/source', '/home/alepy/Folder-Synchronizer/replica', '/home/alepy/Folder-Synchronizer/logs.txt')
