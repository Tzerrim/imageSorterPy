import os
import argparse

# Variables
source_dir = ""
destination_dir = ""
filename_key = ""
pack_copy_flag = False
files_in_folders = 0
file_names = []

keys = ("-s", "-d", "-c", "-p")  # Keys for arguments. -s - source, -d - destination, -c - copy, -p - pack
extensions = (".png", ".jpeg", ".jpg", ".gif")  # File extensions that will process this script


def end_slash_appender(path):

    if not path.endswith("/"):
        path.join("//")
    return path


def move_copy():

    print("Moving files . . . ")
    global source_dir
    global destination_dir
    source_dir = end_slash_appender(source_dir)
    destination_dir = end_slash_appender(destination_dir)
    get_filename_from_source()
    for file in file_names:
        source_file = source_dir+file
        destination_file = destination_dir + file
        os.rename(source_file, destination_file)
    print("Moved: ", len(file_names))


def get_filename_from_source():

    for file in os.listdir(source_dir):
        print("Process file: ", file, " ", file.lower().find(filename_key.lower()))
        if file.endswith(extensions):
            if (filename_key != "" and file.lower().find(filename_key.lower()) >= 0) or filename_key == "":
                print(file.lower().find(filename_key.lower()))
                file_names.append(file)
    print("Files to move: ", len(file_names))


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def get_last_matching_dir():
    directories = get_immediate_subdirectories(destination_dir)
    for i in range(1, len(directories)):
        if i in directories:
            continue
        else:
            return i
    return 1


# Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument('-s', action="store", dest="source_dir", default="")
parser.add_argument('-d', action="store", dest="destination_dir", default="")
parser.add_argument('-f', action="store", dest="filename_key", default="")
parser.add_argument('-p', action="store", dest="files_in_folders", default=0, type=int)

args = parser.parse_args()

source_dir = args.source_dir
destination_dir = args.destination_dir
filename_key = args.filename_key
files_in_folders = args.files_in_folders

if source_dir != "" and destination_dir != "":
    move_copy()
else:
    print("Missing source and/or destination directories path")

