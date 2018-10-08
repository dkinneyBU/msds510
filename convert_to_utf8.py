"""
2. Convert to UTF8 Script
Implement the convert_to_utf8.py script and generate the avengers_utf8.csv file in the interim data directory.
This script should take two command line arguments, an input file and the output file. After you have finished
implementing the script, you should be able to run the script as follows.

python convert_to_utf8.py ../data/raw/avengers.csv ../data/interim/avengers_utf8.csv
"""

import sys


def convert_to_utf(infile, outfile):
    try:
        _infile = open(infile, 'r', encoding='utf-8').read()
        _outfile = open(outfile, 'w')
        _outfile.write(_infile)
    except Exception as e:
        print(e)
    return


def main():
    convert_to_utf(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
