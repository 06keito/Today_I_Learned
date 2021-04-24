#ABC001_A.py → abc001_a.py

import os,glob

path = "sample_name.py"
files = glob.glob(path)

for f in files:
    basename = str.lower(os.path.basename(f))
    os.rename(f,basename)
