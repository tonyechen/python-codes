import os
import shutil # needed to delete files that contains files

path = "folder"

try:
    # os.remove(path)  # remove files
    # os.rmdir(path)  # remove directory
    shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")