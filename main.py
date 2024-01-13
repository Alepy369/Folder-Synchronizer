# main.py
import os
import sys
import logging
import datetime
import time

from sync.sync import (
    get_source_content,
    get_replica_content,
    check_files_and_folders,
    create_file,
    create_dir,
    copy,
    remove,
    to_sync
)

source_path = '/home/alepy/Folder-Synchronizer/source'
replica_path = '/home/alepy/Folder-Synchronizer/replica'
log_file_path= '/home/alepy/Folder-Synchronizer/logs.txt'

def main(source_path, replica_path, sync_interval, log_file_path):

    # print("                                     ")
    # print("=====================================")
    # print("  Welcome to the Folder Synchronizer  ")
    # print("=====================================")
    # print("                                     ")
    # print("  Options:                           ")
    # print("    1 - Create a file or folder      ")
    # print("    2 - Copy a file or folder        ")
    # print("    3 - Remove a file or folder      ")
    # print("                                     ")
    # print("    q - Quit                         ")
    # print("                                     ")
    
    while True:

        list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source, list_file_hash_source=get_source_content(source_path)
        list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica, list_file_hash_replica=get_replica_content(replica_path)

        result = check_files_and_folders(list_file_paths_source, list_dir_paths_source, list_file_paths_replica, list_dir_paths_replica)

        time.sleep(sync_interval * 60)

        # Perform synchronization
        to_sync(result, source_path, replica_path, log_file_path)


if __name__ == "__main__":

    # if len(sys.argv) != 5:
    #     print("Usage: python main.py <source_path> <replica_path> <sync_interval> <log_file_path>")
    #     sys.exit(1)

    source_path = source_path #sys.argv[1]
    replica_path = replica_path #sys.argv[2]
    sync_interval = 0.5 #sys.argv[3]
    log_file_path = log_file_path #sys.argv[4]

    main(source_path, replica_path, sync_interval, log_file_path)
