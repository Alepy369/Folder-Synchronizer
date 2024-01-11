# main.py
import os
import sys
import logging
import datetime

from sync.sync import (
    get_source_content,
    get_replica_content,
    check_files_and_folders,
    create_file,
    create_dir,
    copy,
    remove,
)

source_path = '/home/alepy/Folder-Synchronizer/source'
replica_path = '/home/alepy/Folder-Synchronizer/replica'
log_file_path= '/home/alepy/Folder-Synchronizer/logs.txt'

def main(source_path, replica_path, sync_interval, log_file_path):

    print("                                     ")
    print("=====================================")
    print("  Welcome to the Folder Synchronizer  ")
    print("=====================================")
    print("                                     ")
    print("  Options:                           ")
    print("    1 - Sync folders                 ")
    print("    2 - Check for unsynced items     ")
    print("    3 - Create a file or folder      ")
    print("    4 - Copy a file or folder        ")
    print("    5 - Remove a file or folder      ")
    print("    6 - Periodicaly sync             ")
    print("                                     ")
    print("    q - Quit                         ")
    print("                                     ")
    
    while True:
        option=input('Choose -> ' )

        if option == '1':
            print('Syncing folders...')
    

        elif option == '2':
            print('Checking for unsynced items...')            

            # Get content from source and replica folders
            list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source = get_source_content(source_path)
            list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica = get_replica_content(replica_path)

            # Check content missing in replica folder
            items_not_in_replica=check_files_and_folders(list_file_source, list_file_replica, list_dir_source, list_dir_replica)

            user_input = input('Do you want to sync folders? (y/n) -> ')
            if user_input.lower() == 'y':
                print('Syncing folders...')
                # Add your synchronization logic here

            elif user_input.lower() == 'n':
                pass

            else:
                print('Invalid option. Please choose a valid option.')

            list_file_source.clear()
            list_dir_source.clear()
            list_dir_replica.clear()
            list_file_replica.clear()
            items_not_in_replica = {"Files": [], "Dirs": []}
    

        elif option == '3':
            inpt=input("Creating a file or a folder? ")
            if inpt.lower() == 'file':
                print('Creating file...')
                dir_path=input('Where? (dir path "/home/...") -> ')
                name=input('File name? -> ')
                path=dir_path + "/" + name
                create_file(path, log_file_path)
                print(f'{name} created...')
            elif inpt.lower() == 'folder':
                print('Creating folder...')
                dir_path=input('Where? (full path "/home/...") -> ')
                create_dir(dir_path, log_file_path)
                name=dir_path.split('/')[-1]
                print(f'{name} created...')
            else:
                print('Invalid option. Try again.')
            

        elif option == '4':
            print('Copying a file or folder...')
            path1=input("Source (full path) -> ")
            path2=input("Destination (full path) -> ")
            copy(path1, path2, log_file_path)
            print(f'Source {path1} copied to {path2}')
            

        elif option == '5':
            print('Removing a file or folder...')
            path=input("Full path -> ")
            remove(path, log_file_path)
            name=path.split('/')[-1]
            folder_path=os.path.dirname(path)
            print(f'{name} removed from {folder_path}')
            
            
        elif option == '6':
            print(f'Periodicaly syncing every {sync_interval} minutes...')
            with open(log_file_path) as file:
                lines = file.readlines()
                for line in reversed(lines):
                    if "Initializing Folder Synchronizer" in line:
                        time=line.strip().split(" ")[1]
                        time_stamp=line.strip().split(" ")[0] + " " + line.strip().split(" ")[1]
                        print(f'Starting time: {time}')
                        last_sync_time = datetime.datetime.strptime(time_stamp, "%m/%d/%Y %H:%M:%S")
                        current_time = datetime.datetime.now().replace(microsecond=0, second=0,)

                        current_time_aligned = current_time.replace(year=last_sync_time.year, month=last_sync_time.month, day=last_sync_time.day)

                        print(last_sync_time)
                        print(current_time_aligned)
                        time_difference = current_time_aligned - last_sync_time
                        print(time_difference.total_seconds())
                        if sync_interval == 60 and time_difference.total_seconds() >= 3600:
                            print('Syncing folders...')
                    break
        

        elif option.lower() == 'q':
            print('Quitting...')
            sys.exit(0)
        else:
            print('Invalid option. Please choose a valid option.')



if __name__ == "__main__":

    # if len(sys.argv) != 5:
    #     print("Usage: python main.py <source_path> <replica_path> <sync_interval> <log_file_path>")
    #     sys.exit(1)

    source_path = source_path #sys.argv[1]
    replica_path = replica_path #sys.argv[2]
    sync_interval = 60 #sys.argv[3]
    log_file_path = log_file_path #sys.argv[4]

    main(source_path, replica_path, sync_interval, log_file_path)
