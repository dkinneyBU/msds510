"""
3a. Use Basic CSV Reader
Implement the read_csv.py script. It should take one argument as input, the input CSV file. When completed, you
should be able to run the script as follows. python read_csv.py ..\\data\\interim\\avengers_utf8.csv Use csv.reader to
read the CSV data into rows. Using the print function to print the 162nd row. For the purposes of this exercises,
do not skip the header row.
"""
import csv
import sys

def read_csv_file(file_to_read):
    with open(file_to_read) as csvfile:
        csvreader = csv.reader(csvfile)
        #  Probably not the most efficient way to to this. As csvreader is an iterable reader object,
        #  I didn't think there was a way to directly access the 162nd element (i.e., csvreader[162].
        for i, row in enumerate(csvreader):
            if i == 162: print(', '.join(row))
    return

def main():
    read_csv_file(sys.argv[1])


if __name__ == "__main__":
    main()
