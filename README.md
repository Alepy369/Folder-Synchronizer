# Folder-Synchronizer
A backup program that syncs two different folders periodically, creating logs for every operation (start/create/copy/remove).

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

Attention!
The argument "sync_interval" has to be given in minutes.

```bash
python main.py source_path replica_path sync_interval log_file_path
```
