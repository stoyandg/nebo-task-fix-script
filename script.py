import os
import glob
import sys

# Usage: python3 script.py "absolute/path/to/directory" "*.file-type" "number-of-characters-to-slice"

os.chdir((sys.argv[1]))
for file in glob.glob((sys.argv[2])):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    characters_to_remove = int(sys.argv[3])
    new_file_name = file_name[:-characters_to_remove] + extension
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print(F"Renamed {file} to {new_file_name}")