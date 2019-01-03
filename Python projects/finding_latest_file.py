import os

import glob
import os

search_dir = "/mydir/"
# remove anything from the list that is not a file (directories, symlinks)
# thanks to J.F. Sebastion for pointing out that the requirement was a list
# of files (presumably not including directories)
files = filter(os.path.isfile, glob.glob(search_dir + "*"))
files.sort(key=lambda x: os.path.getmtime(x))