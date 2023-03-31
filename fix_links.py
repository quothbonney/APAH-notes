import os
import time

def search_directory_for_string(start_dir, search_string):
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith('.md'): # change '.txt' to the extension of the files you want to search
                filepath = os.path.join(dirpath, filename)
                lines = None
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                    lines.append("""[[AP Art History]]""")

                with open(filepath, 'w') as file:
                    file.writelines(lines)



search_directory_for_string('.', '![[')
