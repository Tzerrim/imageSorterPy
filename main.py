import os
import argparse

# Variables
source_dir = ""
destination_dir = ""
filename_key = ""
pack_in_folders_flag = False
pack_copy_flag = False
files_in_folders = 0
file_names = []

keys = ("-s", "-d", "-c", "-p") # Keys for arguments. -s - source, -d - destiantion, -c - copy, -p - pack
extensions = (".png", ".jpeg", ".jpg", ".gif") # File extensions that will process this script

def move_copy():
    print("Moving files . . . ")
    global source_dir
    source_dir = endSlashAppender(source_dir)
    getFilenameFromSource()
    for file in file_names:
        source_file = source_dir+file
        destination_file = destination_dir + file
        print("Moving: ", source_file, " To: ", destination_file)
        os.rename(source_file , destination_file)

def getFilenameFromSource():

    for file in os.listdir(source_dir):
        print("Process file: ", file, " ", file.lower().find(filename_key.lower()))
        if file.endswith(extensions):
            if (filename_key != "" and file.lower().find(filename_key.lower())) or filename_key == "":
                file_names.append(file)
    print("Files to move: ", len(file_names))

def fileToFolderPacker():
    pass;

def endSlashAppender (path):
    if not path.endswith("\\"):
        path.join("\\")
    return path


# Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument('-s', action="store", dest="source_dir", default="")
parser.add_argument('-d', action="store", dest="destination_dir", default="")
parser.add_argument('-f', action="store", dest="filename_key", default="")
parser.add_argument('-c', action="store", dest="pack_copy_flag", default=False)
parser.add_argument('-p', action="store", dest="files_in_folders", default=0, type=int)

args = parser.parse_args()
print(args)

source_dir = args.source_dir
destination_dir = args.destination_dir
filename_key = args.filename_key

move_copy()