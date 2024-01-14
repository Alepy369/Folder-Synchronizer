import sys
import time

from sync import initialize_logger # Imports initialize_logger function from __init__.py

# Imports functions from sync.py 
from sync.sync import (
    get_source_content,
    get_replica_content,
    check_files_and_folders,
    to_sync
)

def main(source_path, replica_path, sync_interval, log_file_path):

    start_log = initialize_logger(log_file_path)
    
    while True:

        time.sleep(sync_interval * 60)

        s_path, list_file_paths_source, list_dir_paths_source, list_file_source, list_dir_source, list_file_hash_source=get_source_content(source_path)
        r_path, list_dir_paths_replica, list_file_paths_replica, list_dir_replica, list_file_replica, list_file_hash_replica=get_replica_content(replica_path)

        result = check_files_and_folders(source_path, replica_path, list_file_paths_source, 
                                 list_dir_paths_source, list_file_paths_replica, list_dir_paths_replica)

        to_sync(result, list_file_paths_replica, list_dir_paths_replica, list_file_paths_source,
                 list_dir_paths_source, source_path, replica_path, log_file_path)


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python main.py <source_path> <replica_path> <sync_interval> (in minutes) <log_file_path>")
        sys.exit(1)

    source_path = str(sys.argv[1])
    replica_path = str(sys.argv[2])
    sync_interval = int(sys.argv[3])
    log_file_path = str(sys.argv[4])

    main(source_path, replica_path, sync_interval, log_file_path)
