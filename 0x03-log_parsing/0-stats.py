#!/usr/bin/python3
"""Script to compute and print out metrics."""
import sys


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


def print_stats(status_codes, file_size=0):
    """Print out stats to `stdout`.

    Args:
        status_codes (dict): maps frequency of status codes.
        file_size (int): overall file size seen.
    """
    print("File size: {}".format(file_size))
    for status, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(status, count))


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
