"""my_shell_outline.py:
Simple shell that interacts with the filesystem, e.g., try "PShell>files".

Try to stick to Style Guide for Python Code and Docstring Conventions:
see https://peps.python.org/pep-0008 and https://peps.python.org/pep-0257/

(Note: The breakdown into Input/Action/Output in this script is just a suggestion.)
"""

import glob
import os
import pwd
import shutil
import sys
import time
from datetime import datetime
# ========================
#    files command
#    List file and directory names
#    No command arguments
# ========================
def files_cmd(fields):
    """Return nothing after printing names/types of files/dirs in working directory.
    
    Input: takes a list of text fields
    Action: prints for each file/dir in current working directory their type and name
            (unless list is non-empty in which case an error message is printed)
    Output: returns no return value
    """
    
    if checkArgs(fields, 0):
        for filename in os.listdir('.'):
            if os.path.isdir(os.path.abspath(filename)):
                print("dir:", filename)
            else:
                print("file:", filename)



# ========================
#  info command
#     List file information
#     1 command argument: file name
# ========================

def info_cmd(fields):
   if checkArgs(fields, 1):
        if(os.path.isfile(fields[1])):
            print("File Name:", fields[1])
            print("Directory/File: file")
            print("Size:", os.path.getsize(fields[1]))
            print("Executable?:", os.access(fields[1], os.X_OK))
        else:
            print("Directory/File: directory")
        print("Owner: " + pwd.getpwuid(os.stat(fields[1]).st_uid).pw_name)
        print("Last Edited: " + datetime.fromtimestamp(os.path.getmtime(fields[1])).strftime('%b %d %Y %H:%M:%S'))

def delete_cmd(fields):
    if checkArgs(fields, 1):
        if(os.path.exists(fields[1])):
            os.remove(fields[1])
            print("Successfully deleted")
        else:
            print("File does not exist")

def copy_cmd(fields):
    if checkArgs(fields, 2):
        if(os.path.exists(fields[1])):
            if(os.path.exists(fields[2])== False):
                shutil.copy2(fields[1], fields[2])
            else:
                print("To file already exists")
        else:
            print("From file does not exist")

def where_cmd(fields):
    if checkArgs(fields, 0):
        print(os.getcwd())

def down_cmd(fields):
    directory = (" ".join(fields[1:]))
    if os.path.isdir(directory):
        os.chdir(directory)
    else:
        print("Error directory does not exist")

def up_cmd(fields):
    if checkArgs(fields, 0):
        os.chdir("..")
        
# ----------------------
# Other functions
# ----------------------
def checkArgs(fields, num):
    """Returns if len(fields)-1 == num and print an error in shell if not.
    
    Input: takes a list of text fields and how many non-command fields are expected
    Action: prints error to shell if the number of fields is unexpected
    Output: returns boolean value to indicate if it was expected number of fields
    """

    numArgs = len(fields) - 1
    if numArgs == num:
        return True
    if numArgs > num:
        print("Unexpected argument", fields[num+1], "for command", fields[0])
    else:
        print("Missing argument for command", fields[0])
        
    return False

# ---------------------------------------------------------------------

def main():
    """Returns exit code 0 (after executing the main part of this script).
    
    Input: no function arguments
    Action: run multiple user-inputted commands
    Output: return zero to indicate regular termination
    """
    
    while True:
        line = input("PShell>")
        fields = line.split()
        # split the command into fields stored in the fields list
        # fields[0] is the command name and anything that follows (if it follows) is an argument to the command
        
        if fields[0] == "files":
            files_cmd(fields)
        elif fields[0] == "info":
            info_cmd(fields)
        elif fields[0] == "delete":
            delete_cmd(fields)
        elif fields[0] == "copy":
            copy_cmd(fields)
        elif fields[0] == "where":
            where_cmd(fields)
        elif fields[0] == "down":
            down_cmd(fields)
        elif fields[0] == "up":
            up_cmd(fields)
        elif fields[0] == "exit":
            sys.exit()
        else:
            print("Unknown command", fields[0])
    
    return 0 # currently unreachable code

if __name__ == '__main__':
    sys.exit( main() ) # run main function and then exit
