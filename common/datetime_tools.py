from datetime import datetime
import argparse
from termcolor import colored

format_timestamp_datetime = '\n    {}  ---->  {}'
datetime_format = '%Y-%m-%d %H:%M:%S'
date_format = '%Y-%m-%d'


def parse(args):
    dt = None
    try:
        dt = datetime.strptime(args, datetime_format)
    except BaseException:
        pass
    if dt:
        return dt

    try:
        dt = datetime.strptime(args, date_format)
    except BaseException:
        pass
    return dt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timestamp', type=float, help='timestamp to format')
    parser.add_argument('-d', '--datetime', help='date time to format')
    args = parser.parse_args()

    args_timestamp = args.timestamp

    now = datetime.now()
    print(colored(format_timestamp_datetime.format(now.strftime(datetime_format), str(now.timestamp())), 'green'))

    if args_timestamp:
        if args_timestamp > 9999999999:
            args_timestamp = args_timestamp / 1000
        ts = datetime.fromtimestamp(args_timestamp)
        print(colored(format_timestamp_datetime.format(str(args.timestamp), ts.strftime(datetime_format)), 'green'))

    if args.datetime:
        dt = parse(args.datetime)
        if dt:
            print(colored(format_timestamp_datetime.format(dt.strftime(datetime_format), str(dt.timestamp())), 'green'))


main()
