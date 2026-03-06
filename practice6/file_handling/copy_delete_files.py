import shutil
import os

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")

# Create backup
shutil.copy("sample.txt", "sample_backup.txt")

print("Files copied")

# Delete safely
if os.path.exists("sample_copy.txt"):
    os.remove("sample_copy.txt")
    print("File deleted")