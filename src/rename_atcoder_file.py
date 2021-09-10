# function : ./ABC001_A.py -> ./abc001_a.py

# run
# -> rename_atcoder_file.py

import os,glob

def main():
    path = "sample_name.py"
    files = glob.glob(path)
    for f in files:
        basename = str.lower(os.path.basename(f))
        os.rename(f,basename)

if __name__ == '__main__':
    main()