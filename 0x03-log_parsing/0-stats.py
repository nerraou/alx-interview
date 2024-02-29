#!/usr/bin/python3
""" parse log input """
import re
import fileinput


def is_valid_ip(ip):
    """ check ip address validity """
    bytes = ip.split(".")
    for byte in bytes:
        if int(byte) > 255:
            return False
    return True


def parse_line(line):
    """ parse line """
    regex = r"^((?:\d{1,3}\.){3}\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] \"GET \/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)$"  # nopep8
    result = re.search(regex, line)

    if result is None:
        return None

    ip = result.group(1)
    method = result.group(3)
    file_size = int(result.group(4))

    if not is_valid_ip(ip):
        return None
    methods = ["200", "301", "400", "401", "403", "404", "405", "500"]
    if method not in methods:
        return None

    return {
        "ip": ip,
        "method": method,
        "file_size": file_size
    }


def print_stats(file_size, methods_stats):
    """ print stats details """
    print("File size {}".format(file_size))
    for status, count in methods_stats.items():
        if count > 0:
            print("{}: {}".format(status, count))


def init_methods_stats():
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
    methods_stats = init_methods_stats()
    parsed_count = 0

    try:
        for line in fileinput.input():
            parsed_line = parse_line(line)
            if parsed_line is not None:
                file_size += parsed_line["file_size"]
                methods_stats[parsed_line["method"]] += 1
                parsed_count += 1

            if parsed_count == 10:
                print_stats(file_size, methods_stats)
                parsed_count = 0
    finally:
        print_stats(file_size, methods_stats)
