"""
Wimbledon Champions Data Processing
Estimate: 45 minutes
Actual:
"""

FILENAME = "wimbledon.csv"

def main():
    records = load_data(FILENAME)

def load_data(filename):
    records = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:

        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)

    return records

def process_records