#!/usr/bin/python3
""" parse log input """
import re
import sys


def parse_line(line):
    """ parse line """
    regex = r"^(.+) ?- ?\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] \"GET \/projects\/260 HTTP\/1\.1\" (\w+) (\d+)$"  # nopep8
    result = re.search(regex, line)

    if result is None:
        return None

    ip = result.group(1)
    status = result.group(3)
    file_size = int(result.group(4))

    statuses = ["200", "301", "400", "401", "403", "404", "405", "500"]
    if status not in statuses:
        status = None

    return {
        "ip": ip,
        "status": status,
        "file_size": file_size
    }


def print_stats(file_size, status_stats):
    """ print stats details """
    print("File size: {}".format(file_size))
    for status, count in sorted(status_stats.items()):
        if count > 0:
            print("{}: {}".format(status, count))


def init_status_stats():
    """ initialize methods stats dict """
    return {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }


if __name__ == "__main__":
    file_size = 0
    status_stats = init_status_stats()
    parsed_count = 0

    try:
        for line in sys.stdin:
            parsed_line = parse_line(line)

            if parsed_line is not None:
                file_size += parsed_line["file_size"]
                status = parsed_line["status"]
                if status is not None:
                    status_stats[status] += 1
                parsed_count += 1

            if parsed_count == 10:
                print_stats(file_size, status_stats)
                parsed_count = 0
    finally:
        print_stats(file_size, status_stats)
