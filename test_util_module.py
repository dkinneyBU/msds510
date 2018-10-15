import utils

def main():
    records = [
        dict(year='1988', intro='Jun-88'),
        dict(year='1989', intro='May-89'),
        dict(year='2005', intro='5-May'),
        dict(year='2013', intro='13-Nov'),
        dict(year='2014', intro='14-Jan'),
    ]
    for record in records:
        print("Input Record - {0}".format(record))
        date_joined = str(utils.get_date_joined(record['year'], record['intro']))
        print("Date joined - {0}".format(date_joined))
        since_joined = str(utils.days_since_joined(record['year'], record['intro']))
        print("Days since joined - {0}".format(since_joined))
        print()

if __name__ == "__main__":
    main()
