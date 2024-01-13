import os
import sys
import time

from sync.sync import (
    get_source_content,
    get_replica_content,
    check_files_and_folders,
    to_sync
)

def main(source_path, replica_path, sync_interval, log_file_path):
    
    while True:

        time.sleep(sync_interval * 60)

        s_path, list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source, list_file_hash_source=get_source_content('/home/alepy/Folder-Synchronizer/source')
        r_path, list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica, list_file_hash_replica=get_replica_content('/home/alepy/Folder-Synchronizer/replica')

        result = check_files_and_folders(s_path, r_path, list_file_paths_source, 
                                 list_dir_paths_source, list_file_paths_replica, list_dir_paths_replica)

        to_sync(result, source_path, replica_path, log_file_path)


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python main.py <source_path> <replica_path> <sync_interval> <log_file_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    replica_path = sys.argv[2]
    sync_interval = int(sys.argv[3])
    log_file_path = sys.argv[4]

    main(source_path, replica_path, sync_interval, log_file_path)
