#!/usr/bin/python3

import sys


def print_stats(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val > 0:
            print("{}: {}".format(key, val))


file_size = 0
line_count = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line = line.split()

            if len(line) > 2:
                line_count += 1
                file_size += int(line[-1])
                status_code = line[-2]

                if status_code in status_codes:
                    status_codes[status_code] += 1

                if line_count == 10:
                    print_stats(status_codes, file_size)
                    line_count = 0

    finally:
        print_stats(status_codes, file_size)
