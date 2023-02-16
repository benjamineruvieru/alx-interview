#!/usr/bin/python3

import sys
import re

"""
A module that reads input from stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
- Total file size: File size: <total size>
  where <total size> is the sum of all previous <file size> (see input format above)
- Number of lines by status code:
  possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  if a status code doesn’t appear or is not an integer, don’t print anything for this status code
  format: <status code>: <number>
  status codes should be printed in ascending order
"""

def compute_metrics():
    """
    Reads input from stdin line by line, computes metrics, and prints statistics after every 10 lines or a keyboard interruption.
    """
    # Initialize variables to keep track of metrics
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    # Read input from stdin line by line
    for line in sys.stdin:
        line = line.strip()

        # Parse input line using regex to extract fields
        match = re.search(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+|-)$', line)

        # If input line doesn't match expected format, skip it
        if not match:
            continue

        # Extract fields from input line
        ip_address = match.group(1)
        date = match.group(2)
        status_code = int(match.group(3))
        file_size = int(match.group(4)) if match.group(4) != '-' else 0

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics after every 10 lines or a keyboard interruption
        if line_count % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for status_code in sorted(status_code_counts):
                if status_code_counts[status_code] > 0:
                    print(f'{status_code}: {status_code_counts[status_code]}')

    # Print final statistics at the end of input
    print(f'Total file size: {total_file_size}')
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print(f'{status_code}: {status_code_counts[status_code]}')

if __name__ == '__main__':
    compute_metrics()
