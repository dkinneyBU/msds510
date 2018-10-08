"""
b. Use DictReader
Implement the read_csv_dict.py script. It should take one argument as input, the input CSV file. When completed,
you should be able to run the script as follows. python read_csv_dict.py ..\\data\\interim\\avengers_utf8.csv Instead
of using csv.reader, use csv.DictReader. Using the print function to print the 161th record and the fieldnames.
"""

import csv
import sys


def read_csv_dict(file_to_read):
    with open(file_to_read) as dictfile:
        dictreader = csv.DictReader(dictfile)
        for i, row in enumerate(dictreader):
            if i == 161: print(row)


def main():
    read_csv_dict(sys.argv[1])


if __name__ == "__main__":
    main()
