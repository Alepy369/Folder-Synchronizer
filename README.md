# Folder-Synchronizer
Rest assured, your files are secure. Use Folder-Synchronizer to create checkpoints of your work and avoid any concerns about losing data.

You can run it on:
  - Windows
  - Linux

## Setup & Installation

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

Ensure that you run the program in the repo folder.

```bash
cd path/to/Folder-Synchronizer
```

## Usage

ATTENTION !!!

 - Make sure to use the full paths and to give the "sync_interval" in minutes.

```bash
python main.py full/path/to/source full/path/to/replica sync_interval_minutes full/path/to/log_file
```

## Testing
### Creation
###
If I created a file and a folder in /source, the output should be something like this:
```
Checking Files:
  File: "file_name"
  Hash: "hash_file"
Checking Folders:
  Folder: "folder_name"
Syncing...
  Folder "folder_name" created!
  File "file_name" created!
```

### Copying / Updating
###
If I change the content from an existing file in both folders, the output should be:
```
Checking Files:
  File "file_name" modified!
Checking Folders:
Syncing...
  File "file_name" copied!
```

### Removing 
###
If I remove a file or an empty folder from /source but it's still on /replica, the output should be:
```
Checking Files:
Checking Folders:
Syncing...
  File "file_name" removed!
```
###
If I remove a folder with content from /source but it's still on /replica, the output should be:
```
Checking Files:
Checking Folders:
Syncing...
ALERT!
The folder "folder_name" is not empty, are you sure you want to delete it? (y/n) 
```
###
If you say "yes" it will delete the folder and all its content, printing every file/folder removed from that same folder as well:
```
Checking Files:
Checking Folders:
Syncing...
ALERT!
The folder "folder_name" is not empty, are you sure you want to delete it? (y/n) y
Deleting the folder and all its content...
  Folder "folder_name" not recovered!
  Folder "folder_name" removed!
  (... content removed ...)  
```

### Recovering a nonempty folder
###
If you say "yes" it will ask you if you want to recover it... If you do want to recover the folder and the content enter "y":
```
Checking Files:
Checking Folders:
Syncing...
ALERT!
The folder "folder_name" is not empty, are you sure you want to delete it? (y/n) y
Do you want to recover it? (y/n) y
  Folder "folder_name" recovered!
  (... content removal canceled ...)
  Folder "folder_name" removal canceled!

  CHECK THE REPLICA FOLDER!
(ends running program)
```
###
If you don't want to recover it, enter "n":
```
Checking Files:
Checking Folders:
Syncing...
ALERT!
The folder "folder_name" is not empty, are you sure you want to delete it? (y/n) y
Do you want to recover it? (y/n) n
  Folder "folder_name" not recovered!
  (... content removal canceled ...)
  Folder "folder_name" removal canceled!

  CHECK THE REPLICA FOLDER!
(ends running program)
```
