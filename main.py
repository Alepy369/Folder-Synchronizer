# main.py
import os
import sys
import logging
 
from sync.sync import (
    get_source_content,
    get_replica_content,
    check_files_and_folders,
    log_create,
    log_copy,
    log_remove,
)

source_path = '/home/alepy/Folder-Synchronizer/source'
replica_path = '/home/alepy/Folder-Synchronizer/replica'
log_file_path= '/home/alepy/Folder-Synchronizer/logs.txt'

def main(source_path, replica_path, sync_interval, log_file_path):

    print("=====================================")
    print(" _    _            _                 ")
    print("| |  | |          | |                ")
    print("| |__| | __ _  ___| | __             ")
    print("|  __  |/ _` |/ __| |/ /             ")
    print("| |  | | (_| | (__|   <              ")
    print("|_|  |_|\\__,_|\\___|_|\\_\\             ")
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
            get_source_content(source_path)
            get_replica_content(replica_path)

            # Check content missing in replica folder
            check_files_and_folders()
    
        elif option == '3':
            print('Creating a file or folder...')
            log_create()
    
        elif option == '4':
            print('Copying a file or folder...')
            log_copy()
    
        elif option == '5':
            print('Removing a file or folder...')
            log_remove()
    
        elif option.lower() == 'q':
            print('Quitting...')
            sys.exit(0)
        else:
            print('Invalid option. Please choose a valid option.')



if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python main.py <source_path> <replica_path> <sync_interval> <log_file_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    replica_path = sys.argv[2]
    sync_interval = sys.argv[3]
    log_file_path = sys.argv[4]

    main(source_path, replica_path, sync_interval, log_file_path)
