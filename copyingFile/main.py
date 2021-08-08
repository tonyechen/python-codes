# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
import os

text = "Yoooooooo\nThis is some text\n See ya!"
with open("test.txt", "w") as file:
    file.write(text)

shutil.copyfile("test.txt", "copy.txt") # source, destination
#shutil.copy("test.txt", "copy.txt")