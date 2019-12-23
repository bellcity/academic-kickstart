'''
USAGE:
python clean_post.py folder


'''
import os
import sys
import pathlib
import datetime

### Get all files in the folder
if sys.argv[1]:
    main_folder = sys.argv[1]
else:
    print('No folder supplied')
    sys.exit(1)

file_list = []
current_root = ''
print('Current dir: {}', os.getcwd())

for root, _, filenames in os.walk(input_dir):
    for filename in filenames:
        file_list.append(os.path.join(root, filename))


### Replace whitespace for '_'
for fd in file_list:
    if os.path.isfile(fd):
        try:
            if pathlib.Path(fd).suffix != '.md':
                newname = os.path.join(os.path.split(fd)[0] + os.sep + os.path.split(fd)[1].replace(' ','_'))
                print('Renaming file: {}\nNew name: {}\n\n'.format(fd, newname))
                os.rename(fd, newname)
        except Exception as e:
            print('Error renaming file : {}'.format(fd))
            continue

### Check if there's an image with the name 'featured'
if any("featured." in lower(s) for s in file_list):
    pass
else:
    print('No image selected to be featured')

### Mozjpeg all files (800width)
response = os.input('')

### Check if index.md exists, if not create it
if any("index.md" in lower(s) for s in file_list):
    pass
else:
    pass

### Add images into index.md



