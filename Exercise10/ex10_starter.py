import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# # TODO: Use the glob.glob() function to obtain the list of filenames
for name in glob.glob(hdir + '/*'):
    print(name)

# # TODO: use os.path.getsize to find each file's size
for name in glob.glob(hdir + '/*'):
    print(name)
    print(os.path.getsize(name))

# # TODO: Add a test to only display files that are not zero length
for name in glob.glob(hdir + '/*'):
    if os.path.getsize(name) != 0:
        print(name)

# TODO: Remove the leading directory name(s) from each filename before you print it -
for name in glob.glob(hdir + '/*'):
    print(os.path.basename(name))


